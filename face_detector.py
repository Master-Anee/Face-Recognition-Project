import cv2
import numpy as np
import config
from insightface.app import FaceAnalysis


class FaceDetector:

    def __init__(self, embeddings, names):

        # ================= MODEL =================
        self.app = FaceAnalysis(name=config.MODEL_NAME)

        self.app.prepare(
            ctx_id=config.DEVICE_ID,
            det_size=config.DETECTION_SIZE
        )

        # ================= DATABASE =================
        self.known_embeddings = embeddings
        self.known_names = names

        # ================= INTERNAL =================
        self.frame_count = 0
        self.last_results = []

    def normalize(self, x):
        return x / np.linalg.norm(x)

    def match_face(self, embedding):

        best_name = "Unknown"
        best_score = -1

        for i, known in enumerate(self.known_embeddings):

            score = np.dot(known, embedding)

            if score > best_score:
                best_score = score

                if score > config.MATCH_THRESHOLD:
                    best_name = self.known_names[i]

        return best_name, best_score

    def detect_and_recognize(self, frame):

        self.frame_count += 1

        h, w = frame.shape[:2]

        results = []

        # ================= SKIP FRAMES FOR SPEED =================
        if self.frame_count % config.DETECTION_INTERVAL != 0:
            return self.last_results

        # ================= PREPROCESS =================
        small_frame = cv2.resize(
            frame,
            (0, 0),
            fx=config.FRAME_SCALE,
            fy=config.FRAME_SCALE
        )

        rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        faces = self.app.get(rgb)

        results = []

        # LIMIT NUMBER OF FACES (performance)
        faces = faces[:config.MAX_FACES]

        for face in faces:

            embedding = self.normalize(face.embedding)

            name, score = self.match_face(embedding)

            # bounding box
            x1, y1, x2, y2 = face.bbox

            # scale back to original frame
            x1 = int(x1 / config.FRAME_SCALE)
            y1 = int(y1 / config.FRAME_SCALE)
            x2 = int(x2 / config.FRAME_SCALE)
            y2 = int(y2 / config.FRAME_SCALE)

            results.append({
                "bbox": (x1, y1, x2, y2),
                "name": name,
                "score": float(score)
            })

        self.last_results = results

        return results
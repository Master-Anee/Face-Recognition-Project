import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis
import config


class FaceDatabase:

    def __init__(self):

        self.app = FaceAnalysis(name=config.MODEL_NAME)

        self.app.prepare(
            ctx_id=config.DEVICE_ID,
            det_size=config.DETECTION_SIZE
        )

        self.embeddings = []
        self.names = []

    def normalize(self, embedding):
        return embedding / np.linalg.norm(embedding)

    def load(self):

        print("=" * 50)
        print("Loading Face Database...")
        print("=" * 50)

        total = 0

        for person in os.listdir(config.KNOWN_FACES_DIR):

            person_folder = os.path.join(
                config.KNOWN_FACES_DIR,
                person
            )

            if not os.path.isdir(person_folder):
                continue

            loaded = 0

            for image_name in os.listdir(person_folder):

                image_path = os.path.join(
                    person_folder,
                    image_name
                )

                image = cv2.imread(image_path)

                if image is None:
                    continue

                faces = self.app.get(image)

                if len(faces) == 0:
                    continue

                embedding = self.normalize(
                    faces[0].embedding
                )

                self.embeddings.append(embedding)
                self.names.append(person)

                loaded += 1
                total += 1

            print(f"{person:15} : {loaded} images")

        print("=" * 50)
        print("Database Ready")
        print(f"Total Images : {total}")
        print(f"Persons      : {len(set(self.names))}")
        print("=" * 50)

    def get_database(self):

        return self.embeddings, self.names
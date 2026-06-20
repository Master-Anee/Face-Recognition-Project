import cv2
import config

from camera import Camera
from face_database import FaceDatabase
from face_detector import FaceDetector
from utils import FPSCounter, draw_box, draw_fps, draw_header


def main():

    # ================= LOAD DATABASE =================
    db = FaceDatabase()
    db.load()

    embeddings, names = db.get_database()

    # ================= INIT MODULES =================
    camera = Camera()
    detector = FaceDetector(embeddings, names)
    fps_counter = FPSCounter()

    print("[INFO] System Started Successfully")

    while True:

        frame = camera.read()

        if frame is None:
            continue

        # ================= AI PROCESSING =================
        results = detector.detect_and_recognize(frame)

        # ================= DRAW RESULTS =================
        for face in results:

            draw_box(
                frame,
                face["bbox"],
                face["name"],
                face["score"]
            )

        # ================= FPS =================
        fps = fps_counter.update()

        if config.SHOW_FPS:
            draw_fps(frame, fps)

        draw_header(frame)

        # ================= DISPLAY =================
        cv2.imshow(config.WINDOW_NAME, frame)

        # ================= EXIT =================
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
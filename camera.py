import cv2
import config


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(
            config.CAMERA_INDEX,
            cv2.CAP_DSHOW
        )

        # ================= CAMERA OPTIMIZATION =================
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)

        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.frame_count = 0

    def read(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def release(self):

        self.cap.release()
        cv2.destroyAllWindows()
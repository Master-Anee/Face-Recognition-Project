import cv2
import time
import config


class FPSCounter:

    def __init__(self):
        self.prev_time = time.time()
        self.fps = 0

    def update(self):
        curr_time = time.time()
        diff = curr_time - self.prev_time

        if diff > 0:
            self.fps = 1 / diff

        self.prev_time = curr_time
        return int(self.fps)


def draw_box(frame, bbox, name, score):

    x1, y1, x2, y2 = bbox

    if name != "Unknown":
        color = config.GREEN
    else:
        color = config.RED

    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    label = f"{name} ({score:.2f})"

    cv2.putText(
        frame,
        label,
        (x1, y1 - 10),
        config.FONT,
        config.FONT_SCALE,
        color,
        config.FONT_THICKNESS
    )


def draw_fps(frame, fps):

    cv2.putText(
        frame,
        f"FPS: {fps}",
        (10, 30),
        config.FONT,
        config.FONT_SCALE,
        config.WHITE,
        config.FONT_THICKNESS
    )


def draw_header(frame):

    cv2.putText(
        frame,
        "INDUSTRY FACE RECOGNITION SYSTEM",
        (10, frame.shape[0] - 10),
        config.FONT,
        0.6,
        config.BLUE,
        2
    )
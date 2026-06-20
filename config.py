"""
=========================================================
            Face Recognition System Configuration
=========================================================
"""

# ================= CAMERA =================
CAMERA_INDEX = 0

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

SHOW_FPS = True

# ================= DETECTION =================
FRAME_SCALE = 0.5

# Detect every N frames
DETECTION_INTERVAL = 5

# Minimum recognition confidence
MATCH_THRESHOLD = 0.45

# ================= MODEL =================
MODEL_NAME = "buffalo_l"

# CPU = -1
# GPU = 0
DEVICE_ID = -1

DETECTION_SIZE = (160, 160)

# ================= PATHS =================
KNOWN_FACES_DIR = "known_faces"

# ================= COLORS =================
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ================= FONT =================
FONT = 0
FONT_SCALE = 0.6
FONT_THICKNESS = 2

# ================= WINDOW =================
WINDOW_NAME = "Professional Face Recognition System"

# ================= PERFORMANCE =================
MAX_FACES = 10

ENABLE_MULTITHREAD = True

ENABLE_FACE_TRACKING = False

ENABLE_LOGS = True
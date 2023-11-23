from pathlib import Path
import sys

file_path = Path(__file__).resolve()

root_path = file_path.parent

if root_path not in sys.path:
    sys.path.append(str(root_path))

ROOT = root_path.relative_to(Path.cwd())

IMAGE = 'Image'
WEBCAM = 'Webcam Guidelines'
WEBCAM2 = 'Webcam Labels'

SOURCES_LIST = [IMAGE, WEBCAM, WEBCAM2]

IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'worker.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'worker_detected.jpg'

MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

WEBCAM_PATH = 0
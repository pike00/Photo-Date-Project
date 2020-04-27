import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PHOTOS_DIR = os.path.join(ROOT_DIR, 'photos')
PHOTOS_RAW_DIR = os.path.join(ROOT_DIR,"photos","raw")
PHOTOS_OUT_DIR = os.path.join(ROOT_DIR,"photos","out")
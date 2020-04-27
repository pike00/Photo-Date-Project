from PIL import Image, ImageFilter, ImageEnhance

# import source
from definitions import *

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

from functions import *

# image_filenames_array = os.listdir(PHOTOS_RAW_DIR)
image_filenames_array = os.listdir(PHOTOS_RAW_DIR)[0:5 ]
# image_filenames_array = os.listdir(PHOTOS_RAW_DIR)[350:]

show_images_one_per_row(image_filenames_array,{'left' : 1200, 'upper' : 900, 'right' : 1700, 'lower' : 1250})
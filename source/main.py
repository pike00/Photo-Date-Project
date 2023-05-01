import os

from PIL import Image, ImageFilter, ImageEnhance

from os.path import join

from PIL.ImageFilter import BuiltinFilter

from skimage import io, measure
from skimage.filters import threshold_otsu


import source
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

# image_filenames_array = os.listdir(PHOTOS_RAW_DIR)
from source.definitions import *
from source.functions import *

image_filenames_array = os.listdir(PHOTOS_RAW_DIR)[0:4]


image = Image.open(join(PHOTOS_RAW_DIR, image_filenames_array[2]))

image = image.convert("1")
image = image.filter(ImageFilter.FIND_EDGES)



fig, axes = plt.subplots(1, 1, figsize=(8, 4))

plt.imshow(image)

# ax[0].imshow(image)
# ax[0].set_title("Original")
plt.show()
# ax[1].imshow(grayscale, cmap=plt.cm.gray)
# ax[1].set_title("Grayscale")


# image = Image.open(join(PHOTOS_RAW_DIR, image_filenames_array[0]))
#
# image = crop(image)
#
# image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
# image = image.filter(ImageFilter.SMOOTH)
# image = image.filter(ImageFilter.EDGE_ENHANCE)
# image = image.filter(ImageFilter.SMOOTH)
# image = image.filter(ImageFilter.SMOOTH)
# image = image.filter(ImageFilter.SMOOTH)
#
#
# for hue_min in range(20, 40, 5):
#     for hue_max in range(30, 50, 5):
#         if(hue_min >= hue_max):
#             continue
#         for saturation_min in range(0,50,10):
#             for saturation_max in range(50,100,5):
#                 if (saturation_min >= saturation_max):
#                     continue
#                 for value_min in range(0, 50, 5):
#                     for value_max in range(50, 100, 5):
#                         if (value_min >= value_max):
#                             continue
#                         tmp_image = filter_hsv(image, hue_min, hue_max,
#                                                saturation_min, saturation_max,
#                                                value_min, value_max)
#
#                         text = ocr_image(tmp_image)
#                         if text == "":
#                             continue
#
#                         print(str(hue_min) + "/" +
#                               str(hue_max) + "/" +
#                               str(saturation_min) + "/" +
#                               str(saturation_max) + "/" +
#                               str(value_min) + "/" +
#                               str(value_max) + ": " + text)
#
#
#
#
# image.save(join(PHOTOS_OUT_DIR, "tmp1.jpg"))

# print(image_filenames_array)
# image_filenames_array = os.listdir(PHOTOS_RAW_DIR)[350:]

# show_images_one_per_row(image_filenames_array,{'left' : 1200, 'upper' : 900, 'right' : 1700, 'lower' : 1250})
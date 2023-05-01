import os

from PIL import Image

from source.definitions import *
from source.image_util import *

import matplotlib.pyplot as plt


def filter_hsv(image,
               hue_min, hue_max,
               saturation_min=0, saturation_max=100,
               value_min=0, value_max=100):

    old_pixels = image.load()
    width, height = image.size

    image_filtered = Image.new('1', (width, height))
    new_pixels = image_filtered.load()

    for x_pixel in range(width):  # for every pixel:
        for y_pixel in range(height):
            (red, green, blue) = old_pixels[x_pixel, y_pixel]

            (hue, saturation, value) = rgb_to_hsv(red, green, blue)

            if (hue > hue_min and hue < hue_max and
                    saturation > saturation_min and saturation < saturation_max and
                    value > value_min and value < value_max):
                new_pixels[x_pixel, y_pixel] = 0
            else:
                new_pixels[x_pixel, y_pixel] = 1

    return image_filtered



def crop(image, crop_parameters=None):
    if crop_parameters is None:
        crop_parameters = (1200, 900, 1700, 1250)

    return(image.crop(crop_parameters))




def show_images_one_per_row(filenames, crop_parameters):
    images = []

    plt.ion()
    image_number = 0
    for image_filename in filenames:
        image_dict = {}

        image_raw = Image.open(os.path.join(PHOTOS_RAW_DIR, image_filename))
        # image_dict[image_filename] = image_raw

        image_crop = crop(image_raw, crop_parameters)

        # image_dict["Cropped"] = image_crop

        hue_min = 26
        hue_max = 40
        saturation_min = 50
        saturation_max = 100
        value_min = 50
        value_max = 100

        image_color_filter = filter_hsv(image_crop,
                                        hue_min=hue_min,
                                        hue_max=hue_max,
                                        saturation_min=saturation_min,
                                        saturation_max=saturation_max,
                                        value_min=value_min,
                                        value_m=value_max)
        image_color_filter = image_color_filter.resize((1500,800))

        filtered_string = "Filtered: " + \
                          str(hue_min) + "<h<" + str(hue_max) + " " + \
                          str(saturation_min) + "<s<" + str(saturation_max) + " " + \
                          str(value_min) + "<v<" + str(value_max)

        image_dict[image_fil] = image_crop
        # image_dict[filtered_string] = image_color_filter

        images.append(image_dict)

        image_number += 1

    rows = len(images)
    cols = len(images[0].keys())

    f = plt.figure(figsize=(cols * 4, rows * 3))

    image_index = 1

    for row in range(rows):
        print("================")
        for key in images[row].keys():
            f.add_subplot(rows, cols, image_index)
            plt.imshow(images[row][key])
            plt.title(key)


            print(ocr_image(images[row][key]))

            print("\n\n\n")

            image_index += 1

    plt.show()


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def ocr_image(image):
    return pytesseract.image_to_string(
        image,
    config='--psm 11 -c tessedit_char_whitelist=0123456789')



def show_array_of_filtered_images():  # based on hue, saturation, value

    (left, upper, right, lower) = (1200, 900, 1700, 1250)

    # images = []

    plt.ion()
    image_number = 0

    w, h = 10, 10
    matrix = [[]]

    image_raw = Image.open(os.path.join(PHOTOS_RAW_DIR, "00000002.jpg"))
    image_dict = {}
    # image_dict[image_filename] = image_raw

    image_crop = image_raw.crop((left, upper, right, lower))
    # image_dict["Cropped"] = image_crop

    hue_min = 20
    hue_max = 60
    saturation_min = 30
    saturation_max = 100
    value_min = 50
    value_max = 100

    min_range = range(30, 60, 10)
    max_range = range(70, 100, 10)

    image_index = 1

    rows = len(min_range)
    cols = len(max_range)

    f = plt.figure(figsize=(cols * 4, rows * 3))

    for value_min in min_range:
        for value_max in max_range:
            image_color_filter = filter_hsv(image_crop,
                                            hue_min=hue_min,
                                            hue_max=hue_max,
                                            saturation_min=saturation_min,
                                            saturation_max=saturation_max,
                                            value_min=value_min,
                                            value_max=value_max)

            f.add_subplot(rows, cols, image_index)

            filtered_string = "Filtered: " + \
                              str(value_min) + "<v<" + str(value_max)

            plt.imshow(image_color_filter)

            plt.title(filtered_string)

            image_index += 1

    # plt.show()

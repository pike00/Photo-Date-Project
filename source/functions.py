import os

from PIL import Image

# import source
from definitions import PHOTOS_RAW_DIR

import matplotlib.pyplot as plt


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360

    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100

    return h, s, v


def hsv_to_hsl(h, s, v):
    l = (2 - s) * v / 2

    if l != 0:
        if l != 1:
            s = 0
        elif l < 0.5:
            s = s * v / (l * 2)
        else:
            s = s * v / (2 - l * 2)

    return (h, s, l)


def get_color_filtered_image(image,
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










def show_images_one_per_row(filenames, crop_parameters):
    images = []

    plt.ion()
    image_number = 0
    for image_filename in filenames:
        # if (image_filename != "00000001.jpg"):
        #     continue

        image_dict = {}

        # image_dict['filename'] = image_filename

        image_raw = Image.open(os.path.join(PHOTOS_RAW_DIR, image_filename))
        # image_dict[image_filename] = image_raw

        image_crop = image_raw.crop((crop_parameters['left'],
                                    crop_parameters['upper'],
                                    crop_parameters['right'],
                                    crop_parameters['lower']))

        # image_dict["Cropped"] = image_crop

        hue_min = 26
        hue_max = 40
        saturation_min = 50
        saturation_max = 100
        value_min = 50
        value_max = 100

        image_color_filter = get_color_filtered_image(image_crop,
                                                                       hue_min=hue_min,
                                                                       hue_max=hue_max,
                                                                       saturation_min=saturation_min,
                                                                       value_min=value_min)
        image_color_filter = image_color_filter.resize((1500,800))

        filtered_string = "Filtered: " + \
                          str(hue_min) + "<h<" + str(hue_max) + " " + \
                          str(saturation_min) + "<s<" + str(saturation_max) + " " + \
                          str(value_min) + "<v<" + str(value_max)

        image_dict[filtered_string] = image_color_filter

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
    config='--psm 7')



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
            image_color_filter = get_color_filtered_image(image_crop,
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

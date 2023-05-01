import os
from os.path import join

from exif import Image

from source.definitions import PHOTOS_RAW_DIR



image_filename = join(PHOTOS_RAW_DIR, os.listdir(PHOTOS_RAW_DIR)[1])
print(image_filename)

with open(image_filename, 'rb') as image_file:
    my_image = Image(image_file)

setattr(my_image, "datetime", "1995:05:10 12:00:00")
#https://www.awaresystems.be/imaging/tiff/tifftags/datetime.html
setattr(my_image, "datetime_original", "1995:05:10 12:00:00")
#https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimeoriginal.html
setattr(my_image, "datetime_digitized", "1995:05:10 12:00:00")
#https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimedigitized.html
setattr(my_image, "orientation", "6")
#https://www.awaresystems.be/imaging/tiff/tifftags/orientation.html

for exif_type in dir(my_image):
    try:
        print(exif_type + ": " + getattr(my_image, exif_type))
    except:
        print("Can't get " + exif_type)

with open(image_filename, 'wb') as new_image_file:
    new_image_file.write(my_image.get_file())


# for exif_type in dir(my_image):
#     print(my_image['exif_type'])
#
#

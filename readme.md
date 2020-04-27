# Photo Date Project

This project is dedicated to extracting the text from a series of scanned photos and storing it as exif data for easy classification. The photos were scanned using ScanMyPhotos.com with a resolution of 300 dpi. There are approximately 6000 photos in total to scan.

## Dependencies
The dependencies for this project can be found in requirements.txt, although this isn't accurate because I haven't quite gotten a chance to **really** learn how virtualenvs work.... Definitely required: PIL (Pillow), tesseract.

## Photos

Included are >300 photos that can be used to test on. The photos **generally** have a date in orange text in the bottom corner. The dates may not be in the same absolute location because some photos were scanned upside down. This is fairly straightforward to implement once the OCR part of it is working.

A sample of the photos is available [here](https://georgetown.box.com/s/1hti1kecmc3gx1409nxc6abqtgxj9a10). 

## OCR

My overall strategy has been to load each file, crop in the image to a window slightly larger than where the date is (by trial-and-error), and then filter the image using HSV values to pick out that bright orange that really stands out to the human eye. Who knows if this is the best way, but I've tried contrast, brightness, color filtering with RGB (which is painfully difficult to pick a 'range of colors'...). So far HSV works the best.

Tesseract, while free and open source, is not programatically friendly for some reason. I could get it to read bits and pieces of the numbers, but nothing absolute or reliable.



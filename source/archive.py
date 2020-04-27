# show_images(image_filenames_array)

# image_crop.save('C:/Users/Will Pike/Desktop/Photo Date Project/image_sharpened.jpg', 'JPEG')
#
# credentials = service_account.Credentials.from_service_account_file("C:/Users/Will Pike/Desktop/Photo Date Project/Photo Date Extraction-bbc2ff69e5bd.json")
#
# client = vision.ImageAnnotatorClient(credentials=credentials,dict=)
#
# # The name of the image file to annotate
# file_name = os.path.abspath("C:/Users/Will Pike/Desktop/Photo Date Project/image_sharpened.jpg")
#
# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#
# image = types.Image(content=content)
#
# # Performs label detection on the image file
# response = client.text_detection(image=image)
# texts = response.text_annotations
# # response = client.label_detection(image=image)
# # labels = response.label_annotations
#
# print('Labels:')
# print(texts)

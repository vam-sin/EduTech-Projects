from PIL import Image
from pytesseract import image_to_string
import os


string = image_to_string(Image.open('mess_menu.jpg'))
print(string)



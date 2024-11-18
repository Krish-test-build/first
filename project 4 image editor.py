from PIL import Image, ImageEnhance, ImageFilter
import os


path = './Imgs for project 4'
newpath='/EditedImg for project 4'

for file in os.listdir(path):
    img= Image.open(f"{path}/{file}")
    edit = img.filter(ImageFilter.SHARPEN)

from PIL import Image
from PIL import ImageFilter

with Image.open('img.png') as pic_original:
    pic_blured =pic_original.filter(ImageFilter.GaussianBlur(4))
    pic_blured.save('blured.jpg')
    pic_blured.show()
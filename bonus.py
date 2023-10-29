import os
from PIL import Image, ImageDraw,ImageFont, ImageFilter
files = os.listdir("photos")
for photo in files:
   with Image.open("photos/"+photo) as image:

       draw = ImageDraw.Draw(image)

       font = ImageFont.truetype("fonts/Inter-Regular.otf", 30)

       draw.text((10,10), "шайлушай", font=font, fill="white")

       image.save("result/"+photo)
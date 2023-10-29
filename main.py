from PIL import Image

with Image.open('img.png') as pic_original:
    print('Зображення відкрито\nРозмір:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()

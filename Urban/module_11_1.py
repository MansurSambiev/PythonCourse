from PIL import Image, ImageFilter

img = Image.open('img.jpg')

print(img.format, img.size, img.mode)

blurred = img.filter(ImageFilter.BLUR)

img.show()
blurred.show()

blurred.save('blurred.png')

position = (5, 10, img.width, img.height)
cropped = img.crop(position)
cropped.save('crop.jpg')

size = (128, 128)
new_name = 'mini.jpg'
img.thumbnail(size)
img.save(new_name)
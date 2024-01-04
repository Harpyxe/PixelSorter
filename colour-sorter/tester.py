from PIL import Image, ImageDraw


myImage = Image.open("img/1.png")
width, height = myImage.size
myImage = myImage.rotate(90, expand=True)
#myImage.show()

data = myImage.getdata()

myImage.save("img/2.png","PNG")
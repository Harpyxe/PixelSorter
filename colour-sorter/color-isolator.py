from PIL import Image, ImageDraw


myImage = Image.open("img/1.png")


width, height = myImage.size
##1024 char 32x32
myImage = myImage.convert('HSV')
pix_val = list(myImage.getdata())


new_image=[]
x=0

while x < 1024:

    red_iso2 = pix_val[x]
    red_iso = red_iso2[0]


    if red_iso in range(140, 145):
        print(pix_val[x])
        red_iso.replace(red_iso,120)
        print(pix_val[x])

    new_image.append(pix_val[x])
    x=x+1
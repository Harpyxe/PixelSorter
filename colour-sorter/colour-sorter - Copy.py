from PIL import Image, ImageDraw


myImage = Image.open("img/1.png")
width, height = myImage.size
myImage = myImage.rotate(90, expand=True)
#myImage.show()

data = myImage.getdata()

myImage.save("img/2.png","PNG")



myImage2 = Image.open("img/2.png")

width, height = myImage2.size
##1024 char 32x32
pix_val = list(myImage2.getdata())







new_img=[]

y_pos=0
x_overall_pos=0
x_relative_pos=0
layer_x = []


while y_pos < height:
    x_relative_pos=0

    while x_relative_pos < width:

        curr_int = pix_val[x_overall_pos]
        new_img.append(curr_int)

        x_overall_pos=x_overall_pos+1
        x_relative_pos=x_relative_pos+1

    y_pos=y_pos+1









sort_new_img = sorted(new_img)

#rint(sort_new_img)


im3 = Image.new("RGBA", size=(width,height))

im3.putdata(sort_new_img)
im3.show()
#im3.show()
#im3.rotate(270, expand=True)

im3.save("img/3.png","PNG")

im3.rotate(270, expand=True)
im3.save("img/5.png","PNG")
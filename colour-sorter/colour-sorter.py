from PIL import Image, ImageDraw


myImage = Image.open("img/1.png")


width, height = myImage.size
##1024 char 32x32
pix_val = list(myImage.getdata())







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
im3.save("img/2.png","PNG")
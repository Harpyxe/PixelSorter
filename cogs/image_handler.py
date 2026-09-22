from PIL import Image
import numpy as np
import os



def make_png(input_image):
    with Image.open(input_image) as temp_img:
        temp_img = temp_img.convert("RGB")
        temp_img.save(f"{os.getcwd()}/img/temp_photo.png", format="PNG")
    temp_img.close









#make_png(f"{os.getcwd()}/img/photo.png")

# def load_image(image_to_load):

#     work_image = Image.open(image_to_load)
#     pixels = work_image.load()
#     width, height = work_image.size

#     print(width, height)
#     print("----")
#     #print(pixels)

    
#     for y in range(height):
#         for x in range(width):
#             print(f"{pixels[x, y]}")










#load_image(f"{os.getcwd()}/img/binary_mask.png")     


# def create_lum_mask(input_image):
#     img = Image.open(input_image)
#     arr = np.array(img, dtype=float)  # shape: (height, width, 3)
#     lum = (0.2126*arr[...,0] + 0.7152*arr[...,1] + 0.0722*arr[...,2]).astype(np.uint8)
#     mask = Image.fromarray(lum, mode="L")
#     mask.save(f"{os.getcwd()}/img/mask_photo.png")

# create_lum_mask(f"{os.getcwd()}/img/temp_photo.png")     
from PIL import Image
import numpy as np
import os


def create_lum_mask(input_image, low=100, high=200, reverse=False):

    img = Image.open(input_image).convert("RGB")
    arr = np.array(img, dtype=np.float32)

    # Calculate luminance (Rec. 709)
    lum = 0.2126 * arr[..., 0] + 0.7152 * arr[..., 1] + 0.0722 * arr[..., 2]

    # Create binary mask
    mask = np.where((lum >= low) & (lum <= high), 255, 0).astype(np.uint8)

    # Convert back to PIL Image

    if reverse:
        mask = 255 - mask
        
    mask_img = Image.fromarray(mask, mode="L")
    mask_img.save(f"{os.getcwd()}/img/mask.png")
    #return mask_img



#create_lum_mask(f"{os.getcwd()}/img/temp_photo.png", 110,200)
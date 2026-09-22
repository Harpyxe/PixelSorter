from cogs.image_handler import *
from cogs.mask import *
from cogs.pixel_sorting_logic import *

import time



def sort_workflow(original_image):
    start_time = time.time()

    #make_png(original_image)

    create_lum_mask(original_image, low=90, high=150, reverse=True)

    #sort_by_axis(f"{os.getcwd()}/img/temp_photo.png", f"{os.getcwd()}/img/mask.png", "vertical", False)
    sort_by_axis_numpy(original_image, f"{os.getcwd()}/img/mask.png", axis="horizontal", reverse=True)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program ran for {elapsed_time} seconds")




def sort_by_mask(original_image, mask_image):
    start_time = time.time()

    sort_by_axis_numpy(original_image, mask_image, axis="vertical", reverse=True, save_path=FinsihedPicPath, random_length_min=50, random_length_span=300)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program ran for {elapsed_time} seconds")






BasePicPath = f"{os.getcwd()}/img/1.png"
MaskPicPath = f"{os.getcwd()}/img/mask.png"
FinsihedPicPath = f"{os.getcwd()}/img/sorted_image.png"






#sort_workflow(f"{os.getcwd()}/img/1.jpg")

sort_by_mask(BasePicPath,MaskPicPath)

from PIL import Image
import numpy as np
import os
import random

# def sort_by_axis(image, mask, axis):

#     print(axis)
#     x = 0
#     y = 0
#     active_span = False
#     current_span = []

#     image = Image.open(image)
#     image_pixels = image.load()

#     mask = Image.open(mask)
#     mask_pixels = mask.load()
#     width, height = mask.size

#     for y in range(height):
#         for x in range(width):
#             #print(f"{mask_pixels[x, y]}")

#             if mask_pixels[x, y] == 255:
#                 active_span=True
#                 current_span.append(image_pixels[x, y])

#             else:
#                 print('not current')
#                 active_span = False

#             if active_span == False and current_span:
#                 pixel_list = []
#                 finished_span = []

#                 for pixel in current_span:
#                     pixel_list.append((sum(int(v) for v in pixel), tuple(int(v) for v in pixel)))

#                 pixel_list.sort(key=lambda x: x[0])
#                 for value, rgb in pixel_list:
#                     finished_span.append(rgb)


#                 print(finished_span)

def sort_by_axis(image_path, mask_path, axis, reverse):
    print("Axis:", axis)

    image = Image.open(image_path).convert("RGB")
    image_pixels = image.load()

    mask = Image.open(mask_path).convert("L")
    mask_pixels = mask.load()

    width, height = mask.size


    # Iterate over each row (you could also do columns for axis='y')
    if axis == "horizontal":
        for y in range(height):
            current_span = []
            span_coords = []

            for x in range(width):
                if mask_pixels[x, y] == 255:
                    current_span.append(image_pixels[x, y])
                    span_coords.append((x, y))
                else:
                    if current_span:
                        # Process the span
                        pixel_list = [(sum(pixel), pixel) for pixel in current_span]
                        pixel_list.sort(key=lambda x: x[0])
                        sorted_pixels = [rgb for _, rgb in pixel_list]

                        # Replace original pixels
                        for (px, py), rgb in zip(span_coords, sorted_pixels):
                            image_pixels[px, py] = rgb

                        # Reset for next span
                        current_span = []
                        span_coords = []

            # Process span at end of row if it reaches the edge
            if current_span:
                pixel_list = [(sum(pixel), pixel) for pixel in current_span]
                pixel_list.sort(key=lambda x: x[0])
                sorted_pixels = [rgb for _, rgb in pixel_list]

    elif axis == "vertical":
        for x in range(width):  # iterate over columns
            current_span = []
            span_coords = []


            for y in range(height):  # iterate down the column
                if mask_pixels[x, y] == 255:
                    current_span.append(image_pixels[x, y])
                    span_coords.append((x, y))
                else:
                    if current_span:
                        # Process the span
                        pixel_list = [(sum(pixel), pixel) for pixel in current_span]
                        pixel_list.sort(key=lambda item: item[0])
                        sorted_pixels = [rgb for _, rgb in pixel_list]

                        # Replace original pixels in column
                        for (px, py), rgb in zip(span_coords, sorted_pixels):
                            image_pixels[px, py] = rgb

                        # Reset for next span
                        current_span = []
                        span_coords = []

            # Process span at end of column if it reaches the bottom
            if current_span:
                pixel_list = [(sum(pixel), pixel) for pixel in current_span]
                pixel_list.sort(key=lambda item: item[0], reverse=reverse)
            sorted_pixels = [rgb for _, rgb in pixel_list]



    for (px, py), rgb in zip(span_coords, sorted_pixels):
        image_pixels[px, py] = rgb
    image.save("img/sorted_image.png")

#sort_by_axis(f"{os.getcwd()}/img/temp_photo.png", f"{os.getcwd()}/img/binary_mask.png", "horizontal", False)





def sort_by_axis_numpy(image_path, mask_path, axis="horizontal", reverse=False, save_path=f"{os.getcwd()}/img/sorted_image.png", random_length_min=10,random_length_span=0):
    """
    Sort image pixels along masked spans using NumPy for speed.

    Parameters:
    - image_path: path to RGB image
    - mask_path: path to binary mask (L mode, 0/255)
    - axis: "horizontal" or "vertical"
    - reverse: True for descending, False for ascending
    - save_path: path to save the sorted image
    """
    # Load image and mask
    img = Image.open(image_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")

    img_arr = np.array(img, dtype=np.uint8)       # shape: (H, W, 3)
    mask_arr = np.array(mask, dtype=np.uint8)     # shape: (H, W)

    H, W, _ = img_arr.shape

    if axis == "horizontal":
        for y in range(H):
            row = img_arr[y]
            mask_row = mask_arr[y]
            
            start = None
            current_span_number = 0
            random_span_end_number = np.random.randint(random_length_min, random_length_span)

            for x in range(W + 1):  # +1 to handle edge
                if x < W and mask_row[x] == 255:
                    if start is None:
                        start = x
                        current_span_number = 0
                        random_span_end_number = np.random.randint(random_length_min, random_length_span)

                    current_span_number += 1

                    # --- EARLY END CONDITION ---
                    if random_length_span != 0 and current_span_number >= random_span_end_number:
                        end = x
                        span = row[start:end]

                        # Sort pixels in the span by sum of RGB
                        sums = span.sum(axis=1)
                        order = np.argsort(sums)
                        if reverse:
                            order = order[::-1]
                        sorted_span = span[order]

                        # Replace the original span
                        row[start:end] = sorted_span

                        # Reset for next span
                        start = None
                        current_span_number = 0
                        random_span_end_number = np.random.randint(random_length_min, random_length_span)
                else:
                    if start is not None:
                        end = x
                        span = row[start:end]

                        # Sort pixels in the span by sum of RGB
                        sums = span.sum(axis=1)
                        order = np.argsort(sums)
                        if reverse:
                            order = order[::-1]
                        sorted_span = span[order]

                        # Replace the original span
                        row[start:end] = sorted_span

                        start = None
                        current_span_number = 0


    elif axis == "vertical":

        current_span_number = 0
        random_span_end_number = np.random.randint(random_length_min, random_length_span)

        for x in range(W):
            col = img_arr[:, x, :]
            mask_col = mask_arr[:, x]
            
            start = None
            for y in range(H + 1):
                if y < H and mask_col[y] == 255:
                    if start is None:
                        start = y
                        current_span_number = 0  # reset at start of new span
                        random_span_end_number = np.random.randint(random_length_min, random_length_span)

                    current_span_number += 1

                    # --- EARLY END CONDITION ---

                    if random_length_span != 0 and current_span_number >= random_span_end_number:
                        end = y
                        span = col[start:end]

                        sums = span.sum(axis=1)
                        order = np.argsort(sums)
                        if reverse:
                            order = order[::-1]
                        sorted_span = span[order]
                        col[start:end] = sorted_span

                        # reset span after early end
                        start = None
                        current_span_number = 0
                        random_span_end_number = np.random.randint(random_length_min, random_length_span)

                else:
                    # end of mask region or image
                    if start is not None:
                        end = y
                        span = col[start:end]

                        sums = span.sum(axis=1)
                        order = np.argsort(sums)
                        if reverse:
                            order = order[::-1]
                        sorted_span = span[order]
                        col[start:end] = sorted_span
                        start = None
                        current_span_number = 0

    # Convert back to PIL Image and save
    sorted_img = Image.fromarray(img_arr)
    sorted_img.save(save_path)
    print(f"Saved sorted image as '{save_path}'")


#sort_by_axis_numpy(f"{os.getcwd()}/img/1.webp", f"{os.getcwd()}/img/mask.png", axis="horizontal", reverse=True)
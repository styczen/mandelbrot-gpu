#!/usr/bin/env python
import numpy as np
from constants import * 


def save_pnm_image(image: np.ndarray, file_name: str):
    assert image.dtype == np.uint8, 'Image should be UINT8 format'
    color = len(image.shape) == 3 and image.shape[2] == 3
    image = image.copy().astype(np.uint8)
    with open(file_name, 'wb') as f:
        if color:
            f.write('P6\n'.encode())
        else:
            f.write('P5\n'.encode())
        f.write(f'{image.shape[1]} {image.shape[0]}\n'.encode())
        f.write(f'{255}\n'.encode())
        f.write(image.tobytes())

#def get_color_palette(max_iter: int) -> np.ndarray:
#    palette = np.random.randint(low=0, high=256, size=(MAX_ITER + 1, 3), dtype=np.uint8)
#    palette[-1] = [0, 0, 0]
#    return 

# Source: https://stackoverflow.com/questions/16500656/which-color-gradient-is-used-to-color-mandelbrot-in-wikipedia
def get_color(iteration: int) -> np.ndarray:
    idx = iteration % 16
    palette = [
        [ 66,  30,  15],
        [ 25,   7,  26], 
        [  9,   1,  47],
        [  4,   4,  73], 
        [  0,   7, 100],
        [ 12,  44, 138],
        [ 24,  82, 177], 
        [ 57, 125, 209],
        [134, 181, 229], 
        [211, 236, 248], 
        [241, 233, 191], 
        [248, 201,  95], 
        [255, 170,   0], 
        [204, 128,   0], 
        [153,  87,   0], 
        [106,  52,   3] 
    ]
    return palette[idx]


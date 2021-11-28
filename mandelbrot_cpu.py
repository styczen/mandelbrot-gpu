#!/usr/bin/env python
import time
import numpy as np
from constants import *
from utils import save_pnm_image, get_color


def generate_mandelbrot_set_cpu(width: int, height: int, max_iter: int) -> np.ndarray:
    out_image = np.zeros((height, width, 3), dtype=np.uint8)
    for row in range(height):
        for col in range(width):
            x_0 = M_SET_X[0] + (M_SET_X[1] - M_SET_X[0]) / width * col
            y_0 = M_SET_Y[0] + (M_SET_Y[1] - M_SET_Y[0]) / height * row
            x, y = 0, 0
            iteration = 0
            while x**2 + y**2 <= 2 * 2 and iteration < max_iter:
                x_temp = x**2 - y**2 + x_0
                y = 2 * x * y + y_0
                x = x_temp
                iteration = iteration + 1
            if x**2 + y**2 <= 4:
                out_image[row, col] = [0, 0, 0]
            else:
                out_image[row, col] = get_color(iteration)
    return out_image


if __name__ == '__main__':
    print('Generating Mandelbrot set on CPU')
    start = time.perf_counter()
    out_image = generate_mandelbrot_set_cpu(WIDTH, HEIGHT, MAX_ITER)
    end = time.perf_counter()
    print('Execution time:', end - start, 's')
    save_pnm_image(out_image, 'mandelbrot_set_cpu.pnm')


#!/usr/bin/env python
import time
import numpy as np
from utils import save_pnm_image

# Resolution of image with set visualized
WIDTH = 1500
HEIGHT = 1500

# Mandelbrot set complex plane bounds we want to visualize
M_SET_X = (-2.0, 0.47)
M_SET_Y = (-1.5, 1.5)

# Maximum number of iteration after which we set pixel
# to black i.e. coresponding complex value is in the Mandelbrot set
MAX_ITER = 256

# Randomly generate coloring palette
palette = np.random.randint(low=0, high=256, size=(MAX_ITER + 1, 3), dtype=np.uint8)
palette[-1] = [0, 0, 0]


def get_color(iteration: int) -> np.ndarray:
    return palette[iteration % palette.shape[0]]


def generate_mandelbrot_set() -> np.ndarray:
    out_image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            x_0 = M_SET_X[0] + (M_SET_X[1] - M_SET_X[0]) / WIDTH * col
            y_0 = M_SET_Y[0] + (M_SET_Y[1] - M_SET_Y[0]) / HEIGHT * row
            x, y = 0, 0
            iteration = 0
            while x**2 + y**2 <= 2 * 2 and iteration < MAX_ITER:
                x_temp = x**2 - y**2 + x_0
                y = 2 * x * y + y_0
                x = x_temp
                iteration = iteration + 1
            out_image[row, col] = get_color(iteration)
    return out_image


if __name__ == '__main__':
    start = time.perf_counter()
    out_image = generate_mandelbrot_set()
    end = time.perf_counter()
    print('Execution time:', (end - start) * 1000, 'ms')
    save_pnm_image(out_image, 'mandelbrot_set.pnm')


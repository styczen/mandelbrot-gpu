#!/usr/bin/env python
import time
from mandelbrot_cpu import generate_mandelbrot_set_cpu
from mandelbrot_opencl import generate_mandelbrot_set_opencl
from constants import *


if __name__ == '__main__':
    print('Running CPU implementation')
    start = time.perf_counter()
    out_image_cpu = generate_mandelbrot_set_cpu(WIDTH, HEIGHT, MAX_ITER)
    cpu_time = time.perf_counter() - start
    print('CPU time:', cpu_time, 's')

    print('Running GPU (OpenCL) implementation')
    start = time.perf_counter()
    out_image_gpu = generate_mandelbrot_set_opencl(WIDTH, HEIGHT, MAX_ITER)
    gpu_time = time.perf_counter() - start
    print('GPU time:', gpu_time, 's')


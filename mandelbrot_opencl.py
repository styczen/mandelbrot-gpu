#!/usr/bin/env python
import time
import pyopencl as cl
import numpy as np
from utils import save_pnm_image
from constants import *


def generate_mandelbrot_set_opencl(width: int, height: int, max_iter: int) -> np.ndarray:
    platforms = cl.get_platforms()
    gpu_devs = platforms[0].get_devices(device_type=cl.device_type.GPU)
    dev = gpu_devs[0]
    ctx = cl.Context(devices=[dev])
    with cl.CommandQueue(context=ctx, device=dev) as queue:
        with open('kernel.cl', 'r') as f:
            kernel_source = f.read()
        program = cl.Program(ctx, kernel_source).build()

        # Output parameters
        mf = cl.mem_flags
        result_image_cl = cl.Image(context=ctx,
                                   flags=mf.WRITE_ONLY,
                                   format=cl.ImageFormat(cl.channel_order.RGBA, cl.channel_type.UNSIGNED_INT8),
                                   shape=(width, height),
                                   )

        # Start kernel
        global_size = (width, height)
        local_size = None
        program.mandelbrot_set(queue, global_size, local_size, 
                               np.float32(M_SET_X[0]), np.float32(M_SET_X[1]), 
                               np.float32(M_SET_Y[0]), np.float32(M_SET_Y[1]), 
                               np.int32(max_iter),
                               result_image_cl)
        # Read data from device
        result_np = np.zeros((height, width, 4), dtype=np.uint8)
        cl.enqueue_copy(queue=queue, 
                        dest=result_np, 
                        src=result_image_cl, 
                        origin=(0, 0),
                        region=global_size,
                        is_blocking=True)
    return result_np[:, :, 0:3] 



if __name__ == '__main__':
    print('Generating Mandelbrot set on GPU using OpenCL kernel language')
    start = time.perf_counter()
    out_image = generate_mandelbrot_set_opencl(WIDTH, HEIGHT, MAX_ITER)
    end = time.perf_counter()
    print('Execution time:', end - start, 's')
    save_pnm_image(out_image, 'mandelbrot_set_gpu.pnm')


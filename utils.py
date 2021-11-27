#!/usr/bin/env python
import numpy as np
import cv2


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


# (c) 2020 B. Koch
# This code is licensed under MIT license (see LICENSE.txt for details)

import scipy.ndimage.filters as imagefilter
import numpy as np

IMG_WIDTH = 64
IMG_HEIGHT = 64

sharpen = np.array((
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]), dtype="int")

sharpen = np.flip(sharpen)
print(sharpen)
res = []
for i in range(IMG_HEIGHT):
    res.append(np.arange(IMG_WIDTH*i, IMG_WIDTH*(i+1), dtype=np.uint8))

res = np.array(res)
conv2d = imagefilter.convolve(res, sharpen, mode='constant')
conv2d = conv2d.astype(np.uint8)
conv2d.tofile('data_py.bin')

pass
import numpy as np
from scipy.signal import convolve2d

# Image
I = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Kernel
K = np.array([
    [0.1, 0.1, 0.1],
    [0.1, 0.4, 0.1],
    [0.1, 0.1, 0.1]]
             )

# Perform 2D convolution
result = convolve2d(I, K, mode='valid')
print(result)
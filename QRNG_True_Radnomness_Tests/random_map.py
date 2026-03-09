# dd if=/dev/random of=testdata1.bin bs=1M count=25

import numpy as np
from PIL import Image

# 1. Load the random data we generated earlier
with open("testdata1.bin", "rb") as f:
    # Read exactly 1,000,000 bytes for a 1000x1000 image
    data = f.read(1000 * 1000)

# 2. Convert the byte string into a 2D numpy array (a matrix)
# Each byte becomes one pixel value
pixel_array = np.frombuffer(data, dtype=np.uint8).reshape((1000, 1000))

# 3. Create and save the image
img = Image.fromarray(pixel_array, 'L') # 'L' stands for 8-bit Luminous (Grayscale)
img.save("random_map.png")
print("Image saved as random_map.png")


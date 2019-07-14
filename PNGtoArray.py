from PIL import Image
import numpy as np

i = Image.open('1.png')
iar = np.asarray(i)
print(iar)
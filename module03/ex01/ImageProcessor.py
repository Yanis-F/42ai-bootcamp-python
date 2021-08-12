from PIL import Image
import numpy as np

class ImageProcessor:
    def load(path: str):
        im = Image.open(path)
        print(f"Loading image of dimensions {im.size[0]} x {im.size[1]}")
        return np.asarray(im)

    def display(array):
        print(array)
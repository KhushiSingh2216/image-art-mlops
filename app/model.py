from PIL import Image
import numpy as np
from scipy.ndimage import uniform_filter

# grayscale (same as your code)
def to_grayscale(img_np):
    return np.dot(img_np[..., :3], [0.299, 0.587, 0.114])

# invert
def invert(gray):
    return 255 - gray

# blur (same as your uniform_filter)
def blur_image(inverted):
    return uniform_filter(inverted, size=21)

# dodge blend (your function)
def dodge(front, back):
    return np.clip(front * 255 / (255 - back + 1e-5), 0, 255)

# full sketch pipeline (same steps you wrote)
def pencil_sketch(img_np):
    gray = to_grayscale(img_np)
    inverted = invert(gray)
    blurred = blur_image(inverted)
    sketch = dodge(gray, blurred)
    return sketch.astype(np.uint8)

# ink (your threshold logic)
def ink_sketch(sketch):
    return np.where(sketch < 230, 0, 255).astype(np.uint8)

# cartoon (your logic)
def cartoon_effect(img_np):
    gray = to_grayscale(img_np)
    cartoon = gray.copy()
    cartoon[cartoon < 100] = 0
    cartoon[cartoon >= 100] = 255
    return cartoon.astype(np.uint8)
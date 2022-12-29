import cv2
from PIL import Image
import numpy as np


def f_fuc(u):
    xx = u * (1-u)
    return xx


def tensor2img_numpy(tensor):
    image_numpy = tensor[0].cpu().float().numpy()
    im = (np.transpose(image_numpy, (1, 2, 0))*255).astype('uint8')
    return im


def tensor2img_numpy_hsv(tensor):
    image_numpy = tensor[0].cpu().float().numpy()
    im = (np.transpose(image_numpy, (1, 2, 0))*255).astype('uint8')
    rgb_img = cv2.cvtColor(im, cv2.COLOR_HSV2RGB)
    return rgb_img


def save_images(tensor, path, is_numpy=False):
    if is_numpy:
        im = Image.fromarray(np.uint8(tensor))
    else:
        image_numpy = tensor2img_numpy(tensor)
        im = Image.fromarray(np.uint8(image_numpy))
    im.save(path, 'png')
from numpy import arange
import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os


def f_fuc(u):
    xx = u * (1-u)
    return xx


def tensor2img_numpy(tensor):
    image_numpy = tensor[0].cpu().float().numpy()
    im = np.clip(image_numpy * 255.0, 0, 255.0).astype('uint8')
    return im


def save_images(tensor, path, is_numpy=False):
    if is_numpy:
        im = Image.fromarray(np.uint8(tensor.transpose(1, 2, 0)))
    else:
        image_numpy = tensor2img_numpy(tensor)
        im = Image.fromarray(np.uint8(image_numpy))
    im.save(path, 'png')


path = r'The file path of your test data'
for filename in os.listdir(path):
    img_path = path + '/' + filename
    img = Image.open(img_path)
    img = img.convert('RGB')
    img1 = transforms.ToTensor()(img).unsqueeze(0)
    
    img2 = img1 + f_fuc(img1) 
    x = []
    x.append(img2)

    if torch.mean(img1) <= 0.5:
        c = 1
    else:
        c = -1

    for t in arange(1):
        x[t] = img1 + c * f_fuc(img1) + c * f_fuc(x[t-1]) 
        x.append(x[t])
    
    enhance = tensor2img_numpy(x[-1])
    enhance = np.ascontiguousarray(enhance)
    save_path = r'The path where you want to save the test results' + '/' + filename
    save_images(enhance, save_path, is_numpy=True)
    print(c)
    print(filename+'done!')



import cv2
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

path = r'./Input'
outpath = r'./result'
COLORSPACE = 'HSV'  #'RGB' or 'HSV' / Select Color Space for Under Exposure
INDICAtOR1 = 0.95  #c1
INDICATOR2 = -0.65  #c2
OUTER_ITERN = 2   #T
INNER_ITERN = [1,1]  #K
ISINNER = 1
is_transition = False

for filename in os.listdir(path):
    img_path = path + '/' + filename
    img = Image.open(img_path)
    img = img.convert('RGB')
    imgx =  transforms.ToTensor()(img).unsqueeze(0)
    y = imgx
        
    if COLORSPACE == 'HSV' and torch.mean(y) <= 0.5:
        is_transition = True 
        im = np.array(img)
        img = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
        imgx =  transforms.ToTensor()(img).unsqueeze(0)
        y = imgx[:,2,:,:].unsqueeze(0)
        img_HS = imgx[:,:2,:,:]
        
    
    if torch.mean(y) <= 0.5:
        indicator = INDICAtOR1
    else:
        indicator = INDICATOR2

    outer_iterN = OUTER_ITERN
    inner_iterN = INNER_ITERN

    fy = y * (1-y)
    x =  y + indicator*fy
    Isinner = ISINNER

    for outer_iter in arange(outer_iterN):
        x0 = x
        if Isinner == 1:
            for inner_iter in arange(inner_iterN[outer_iter]):
                    fx = x*(1-x)
                    x = x0 + indicator*fx
        else:
            x = x0

    if is_transition:
        enhance = tensor2img_numpy_hsv(torch.cat((img_HS,x),1))
    else:
        enhance = tensor2img_numpy(x)

    enhance = np.ascontiguousarray(enhance)
    save_path = outpath + '/' + filename
    
    save_images(enhance,save_path , is_numpy=True)

    print(filename + ' done!')
    is_transition = False




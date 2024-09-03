import os
from numpy import arange
import torch
import torchvision.transforms as transforms
from Function import *

# Underexposure correction parameter example
path = r'./Input/under'
outpath = r'./Result'
colorspace = 'HSV'  # 'RGB' or 'HSV' 
indicator = 0.55 # c
outer_itern = 4   # T
inner_itern = [1, 1, 1, 1]  # K
isinner = 1

'''
# Overexposure correction parameter example
path = r'./Input/over'
outpath = r'./Result'
colorspace = 'RGB'  # 'RGB' or 'HSV' 
indicator = 0.65 # c
outer_itern = 2   # T
inner_itern = [2, 2]  # K
isinner = 1
'''


def pec(img_path, save_path, prompt):
    img = Image.open(img_path)
    img = img.convert('RGB')
    if colorspace == 'RGB' :
        imgx = transforms.ToTensor()(img).unsqueeze(0).cuda()
        y = imgx
    elif colorspace == 'HSV' :
        is_transition = True
        im = np.array(img)
        img = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
        imgx = transforms.ToTensor()(img).unsqueeze(0).cuda()
        y = imgx[:, 2, :, :].unsqueeze(0)
        img_HS = imgx[:, :2, :, :]

    fy = y * (1 - y)
    x = y + prompt * indicator * fy

    for outer_iter in arange(outer_itern):
        x0 = x
        if isinner == 1:
            for inner_iter in arange(inner_itern[outer_iter]):
                fx = x * (1 - x)
                x = x0 + prompt * indicator * fx
        else:
            x = x0

    if colorspace == 'RGB':
        enhance = tensor2img_numpy(x)
    elif colorspace == 'HSV':
        enhance = tensor2img_numpy_hsv(torch.cat((img_HS,x),1))


    enhance = np.ascontiguousarray(enhance)

    save_images(enhance, save_path, is_numpy=True)

    print(save_path + ' done!')

def main():
    for filename in os.listdir(path):
        prompt = 1
        img_path = path + '/' + filename
        save_path = outpath + '/' + filename

        img = np.array(Image.open(img_path))
        img = img / 255.0
        pixel_mean = np.mean(img)

        if pixel_mean > 0.5:
            prompt = -1
        
        pec(img_path, save_path, prompt)

if __name__ == '__main__':
    main()




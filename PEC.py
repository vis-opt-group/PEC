import os
from numpy import arange
import torch
import torchvision.transforms as transforms
from Function import *
from Config import cfg


def main():
    is_transition = False
    for filename in os.listdir(cfg.path):
        img_path = cfg.path + '/' + filename
        img = Image.open(img_path)
        img = img.convert('RGB')
        imgx = transforms.ToTensor()(img).unsqueeze(0)
        y = imgx

        if cfg.COLORSPACE == 'HSV' and torch.mean(y) <= 0.5:
            is_transition = True
            im = np.array(img)
            img = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
            imgx = transforms.ToTensor()(img).unsqueeze(0)
            y = imgx[:, 2, :, :].unsqueeze(0)
            img_HS = imgx[:, :2, :, :]


        if torch.mean(y) <= 0.5:
            indicator = cfg.INDICATOR1
        else:
            indicator = cfg.INDICATOR2

        outer_iterN = cfg.OUTER_ITERN
        inner_iterN = cfg.INNER_ITERN

        fy = y * (1 - y)
        x = y + indicator * fy
        Isinner = cfg.ISINNER

        for outer_iter in arange(outer_iterN):
            x0 = x
            if Isinner == 1:
                for inner_iter in arange(inner_iterN[outer_iter]):
                    fx = x * (1 - x)
                    x = x0 + indicator * fx
            else:
                x = x0

        if is_transition:
            enhance = tensor2img_numpy_hsv(torch.cat((img_HS, x), 1))
        else:
            enhance = tensor2img_numpy(x)

        enhance = np.ascontiguousarray(enhance)
        save_path = cfg.outpath + '/' + filename

        save_images(enhance, save_path, is_numpy=True)

        print(filename + ' done!')
        is_transition = False


if __name__ == '__main__':
    main()




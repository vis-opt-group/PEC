


function im = save_images(tensor, path, is_numpy)
if nargin < 3
    is_numpy = false; % 设置默认值
end

if is_numpy
    im = im2uint8(tensor); % 将张量转换为图像（unit8格式）
else
    image_numpy = f_fuc(tensor, 1); 
    im = im2uint8(image_numpy); % 将 Numpy 数组转换为 uint8 类型图像
end

imwrite(im, path);
end
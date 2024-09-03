

function img = f_fuc(tensor, idx)
if idx == 1
    img = tensor2img_numpy(tensor);
else
    img = tensor2img_numpy_hsv(tensor);
end
end


function im = tensor2img_numpy(tensor)
image_tensor = squeeze(tensor(1, :, :, :));
im = uint8(image_tensor * 255);% 将像素值缩放到 0 到 255 之间，并转换为 uint8 类型
end

function rgb_img = tensor2img_numpy_hsv(tensor)  % 将张量转换为RGB图的数组形式，HSV→RGB
image_tensor = squeeze(tensor(1, :, :, :)); % 可能需要根据实际情况调整索引
image_matlab = permute(image_tensor, [2, 3, 1]); % 调整维度顺序
rgb_img = hsv2rgb(image_matlab);
rgb_img = uint8(rgb_img * 255);% 将像素值缩放到 0 到 255 之间，并转换为 uint8 类型
end

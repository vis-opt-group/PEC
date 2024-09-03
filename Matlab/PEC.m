
path = 'Input\under\';
outpath = 'Result\';
colorspace = 'HSV';  % 'RGB' or 'HSV' 
indicator = 0.55;  % c
outer_itern = 4;   % T
inner_itern = [1, 1, 1, 1];  % K
isinner = 1;

filenames = dir(fullfile(path, '*.JPG'));

for i = 1: length(filenames)
    prompt = 1;
    filename = filenames(i).name
    img_path = sprintf('%s%s', path, filenames(i).name);
    save_path = sprintf('%s%s', outpath, filenames(i).name);
    img = imread(img_path); 
    
    img = im2double(img); 

    pixel_mean = mean(img(:));
    if pixel_mean > 0.5
        prompt = -1;
    end
    % d = size(img)

    if strcmp(colorspace, 'RGB')  
        imgx = reshape(img, [1, size(img)]); 
        y = imgx; 

    elseif strcmp(colorspace, 'HSV')
        is_transition = true;
        imgx = rgb2hsv(img);
        imgx = permute(imgx, [3, 1, 2]); 
        imgx = reshape(imgx, [1, size(imgx)]); 
        y = squeeze(imgx(:, 3, :, :));  
        y = reshape(y, [1, size(y)]);

        y = reshape(y, [1, size(y)]); 
        img_HS = imgx(:, 1:2, :, :);  


    end


    fy = y .* (1 - y);
    x = y + prompt * indicator * fy;


    for outer_iter = 1: outer_itern
        x0 = x;
        if isinner == 1
            for inner_iter = 1: inner_itern(outer_iter)
                fx = x .* (1 - x);
                x = x0 + prompt * indicator * fx;
            end   
        else
            x = x0;
        end
    end


    if strcmp(colorspace, 'RGB')
        enhance = f_fuc(x, 1);
    elseif strcmp(colorspace, 'HSV')
        enhanced_img = cat(2, img_HS, x);
        enhance = f_fuc(enhanced_img, 2);
    end

    
    is_numpy = true;
    save_images(enhance, save_path, is_numpy);  
    
    fprintf('%s done!\n', save_path);  


end
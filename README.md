# Practical Exposure Correction: Great Truths Are Always Simple
![visitors](https://visitor-badge.glitch.me/badge?page_id=vis-opt-group/PEC) 

[[Paper](1https://openaccess.thecvf.com/content/CVPR2022/html/Ma_Toward_Fast_Flexible_and_Robust_Low-Light_Image_Enhancement_CVPR_2022_paper.html)] 

<img src="Figs/Firstfig.png" width="1200px"/> 
<p style="text-align:justify">Practicability evaluation. In (a), we compare nine advanced deep networks and nine traditional methods (please refer to the
experimental part for detailed sources) by using different computational resources. In (b), we demonstrate a group of visual comparisons
among two deep networks and PEC on the same scene [3] but with different exposure conditions (the left top and right bottom are
overexposure and underexposure, respectively). In (c), we show visual comparisons among two traditional methods and PEC on different
scenes [9, 24] with different degrees of underexposure. Obviously, our PEC realizes the best visual effects and spends least running time
simultaneously, which fully indicates the practicability of PEC.


## Codes
### Requirements
* python3.7
* pytorch==1.8.0
* cuda11.1

### Testing
* Prepare the data and put it in './Input/'
* Choose a specific model as needed (difficult.pt, medium.pt or easy.pt)
* Run "PEC.py"

## Results on Low-light Image Enhancement
<img src="Figs/LLIE_1.png" width="900px"/> 
<img src="Figs/LLIE_3.png" width="900px"/> 

## Results on High-level Vision Tasks
### Dark Face Detection
<img src="Figs/Det_1.png" width="900px"/> 

### Nighttime Semantic Segmentation
<img src="Figs/Seg_1.png" width="900px"/> 





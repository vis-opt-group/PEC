# Practical Exposure Correction: Great Truths Are Always Simple
![visitors](https://visitor-badge.glitch.me/badge?page_id=vis-opt-group/PEC) 

[[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Ma_Toward_Fast_Flexible_and_Robust_Low-Light_Image_Enhancement_CVPR_2022_paper.html)] [Supplement Material]
<img src="Figs/Fig1.png" width="900px"/>
<p style="text-align:justify"> Practicability evaluation. In (a), we compare nine advanced deep networks and nine traditional methods (please refer to the experimental part for detailed sources) by using different computational resources. In (b), we demonstrate a group of visual comparisons among two deep networks and PEC on the same scene but with different exposure conditions (the left top and right bottom are overexposure and underexposure, respectively). In (c), we show visual comparisons among two traditional methods and PEC on different scenes with different degrees of underexposure. Obviously, our PEC realizes the best visual effects and spends least running time simultaneously, which fully indicates the practicability of PEC.</p>

## Codes
### Requirements
* python3.7
* pytorch==1.8.0
* cuda11.1

### Testing
* Prepare your data for testing and modify the relevant path in "pec.py"
* Adjust the parameters "c" and "t" according to your test data
* Run "pec.py" (Note that we also provide a version of the code for the HSV image domain, namely "pec_hsv.py", whose testing process is the same as above)

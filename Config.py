from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from easydict import EasyDict

# ------------UnderExposure-----------------
_C = EasyDict()
cfg = _C
_C.path = r'./Input/under'
_C.outpath = r'./Result'
_C.COLORSPACE = 'HSV'  # 'RGB' or 'HSV' 
_C.INDICATOR = 0.55  # c
_C.OUTER_ITERN = 4   # T
_C.INNER_ITERN = [1, 1, 1, 1]  # K
_C.ISINNER = 1
# ------------OverExposure-----------------
_D = EasyDict()
cfg_ = _D
_D.path = r'./Input/over'
_D.outpath = r'./Result'
_D.COLORSPACE = 'RGB'  # 'RGB' or 'HSV' 
_D.INDICATOR = -0.6  # c
_D.OUTER_ITERN = 2   # T
_D.INNER_ITERN = [2, 2]  # K
_D.ISINNER = 1



from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from easydict import EasyDict


_C = EasyDict()
cfg = _C
_C.path = r'./Input'
_C.outpath = r'./Result'
_C.COLORSPACE = 'HSV'  # 'RGB' or 'HSV' / Select Color Space for Under Exposure
_C.INDICATOR1 = 0.95  # c1
_C.INDICATOR2 = -0.65  # c2
_C.OUTER_ITERN = 2   # T
_C.INNER_ITERN = [1, 1]  # K
_C.ISINNER = 1


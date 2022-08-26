# oy
# gonna parse some gimp palettes 

# IMPORT STATEMENTS{{{

import re   # regular expressions
import matplotlib   #matlab-like plotting 
from matplotlib import pyplot as plt
import numpy as np  # make python do arrays like matlab
import colorsys     # convert values between colorspaces 
from PIL import Image   # export palettes as images so you can preview your work
import gimp_palette_parse as gpp # module file I wrote 
# }}}
# MAIN{{{
file_path = '../Bears.gpl' # This will eventually be user input
palette1 = gpp.Colors(file_path)
int_colors = palette1.int_colors
float_rgb_colors = palette1.float_colors
hsv_colors = gpp.list_float_to_int(palette1.hsv_colors)
im_hsv = Image.new('HSV',(16,16))
im_hsv.putdata(hsv_colors)
im_hsv.show()
# SORTING{{{
partition_start = 0
partition_end = 128
sorted_int_colors = sorted(int_colors[partition_start:partition_end],key=lambda
        x:x[0],reverse=True) +  int_colors[partition_end + 1:]
# }}}
#  # IMAGE LIBRARY IMAGE{{{
#  sorted_int_tup = []
#  for c in sorted_int_colors:
#      sorted_int_tup.append(tuple(c))
#  img = Image.new('RGB',(16,16))
#  #
#  img.putdata(sorted_int_tup)
#  #
#  img = img.resize((256,256),resample=4)
#  img.show()# }}}
 #    }}}



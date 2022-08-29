# oy
# gonna parse some gimp palettes 

#  IMPORT STATEMENTS{{{

import re   # regular expressions
import matplotlib   #matlab-like plotting 
from matplotlib import pyplot as plt
import numpy as np  # make python do arrays like matlab
import colorsys     # convert values between colorspaces 
from PIL import Image, ImageColor   # export palettes as images so you can preview your work
import gimp_palette_parse as gpp # module file I wrote 
# }}}

# MAIN{{{
file_path = '../Cranes.gpl' # This will eventually be user input
palette1 = gpp.Colors(file_path)
int_colors = palette1.int_colors
float_rgb_colors = palette1.float_colors
hsv_colors = gpp.list_float_to_int(palette1.hsv_colors)
str_colors = palette1.str_colors
pal = palette1.palette
#  im_hsv = Image.new('HSV',(16,16))
#  im_hsv.putdata(hsv_colors)
#  im_hsv.show()

# SORTING{{{
#  red_sorted = gpp.rgb_sort(int_colors,'r',True,(0,256))
#  #  red_sorted_bgr = []
#  #  for item in red_sorted:
#  #      temp = list(item)
#  #      item = tuple(temp[::-1])
#  #      red_sorted_bgr.append(item)
#  #  print(red_sorted)
#  #  print(red_sorted_bgr)
#  red_img = Image.new('RGB',(16,16))
#  red_img.putdata(red_sorted)
#  red_img.resize((256,256),resample=4)
#  red_img.show()
#
#
#  green_sorted = gpp.rgb_sort(int_colors,'g',True,(65,128))
#  green_img = Image.new('RGB',(16,16))
#  green_img.putdata(green_sorted)
#  green_img.resize((256,256),resample=4)
#  green_img.show()
#
#
im = Image.frombytes(mode='RGB',size=(16,15),data=pal.tobytes())
im.show()
# }}}
#  # IMAGE LIBRARY IMAGE{{{
#  sorted_int_tup = []
#  for c in sorted_int_colors:
#      sorted_int_tup.append(tuple(c))
#  img = Image.new('RGB',(1:6,16))
#  #
#  img.putdata(sorted_int_tup)
#  #
#  img = img.resize((256,256),resample=4)
#  img.show()# }}}
 #    }}}



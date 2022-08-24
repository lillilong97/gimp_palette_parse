# oy
# gonna parse some gimp palettes 

import re
import matplotlib
# from colormath.color_objects import sRGBColor, LabColor
# from colormath.color_diff import delta_e_cie1976
from matplotlib import pyplot as plt
from matplotlib import image as mpimg 
import numpy as np
# import custom_color_palette as ccp
import colorsys
import random as rand
from PIL import Image
# CLASS DEFS{{{
class Color:

    def __init__(self,RGB):
        self.RGB = RGB
        self.name = ""

class Palette: 

    def __init__(self,name,colors):
        sRGB = list()
        self.name = name
        self.colors = colors
        for c in colors:
            sRGB.append(make_sRGB(c))
        self.sRGB = sRGB

    def print_pal(self):
        print('Name: ',name)
        for color in colors:
            print(color.RGB)
   
       #
# class RGB:
#
#     def __init__(self,RGB_raw):
#         self.RGB_raw = RGB_raw
#         self.RGB = parse_RGB(RGB_raw)
#
#     def set_RGB(RGB_raw):
#         self.RGB_raw = RGB_raw
        # self.RGB = parse_RGB(RGB_raw)
# }}}
# FUNCTION DEFS{{{
def parse_RGB(RGB_raw):
    RGB = RGB_raw.strip().split()

    for i in range(3):
        RGB[i] = int(RGB[i])

    return RGB
#
#
# def make_sRGB(color):
#     RGB = color.RGB
#     r = RGB[0]
#     g = RGB[1]
#     b = RGB[2]
#
    # return sRGBColor(r,g,b,True)

def float_to_int(float_in):
    return int(float*255)

def int_to_float(int_in):
    return float(int_in/255)

def list_float_to_int(list_in):
    int_list_out = []
    for item in list_in:
        if type(item) is list:
            list_float_to_int(item)
        elif type(item) is float:
            int_list_out.append(float_to_int(item))
    return int_list_out

def list_int_to_float(list_in):
    float_list_out = []
    for item in list_in:
        if type(item) is list:
            list_int_to_float(item)
        elif type(item) is int:
           float_list_out.append(int_to_float(item))     
    return float_list_out

def str_colors_to_int(str_colors):
       int_colors = list()
       for c in str_colors: 
           temp = []
           for val in c:
               temp.append(int(val)) 
           int_colors.append(tuple(temp))
       return int_colors

def list_rgb_to_hsv(float_colors):
    hsv_colors = []
    for i in float_colors:
        hsv_colors.append(tuple(colorsys.rgb_to_hsv(i[0],i[1],i[2])))
    for tup in hsv_colors:
        count = 0
        temp = []
        for num in tup:
            temp.append(int(num*255))
            count = count + 1
        tup = tuple(temp)
    return hsv_colors
     

# }}}
# MAIN{{{

filepath = 'Bears.gpl'
colors = list() 
regex = re.compile(r'^\s*\d*\s*\d*\s*\d')
name_regex = re.compile(r'Name: (.*)')
with open(filepath) as gpl_file:
    header = gpl_file.readline()
    name_line = gpl_file.readline()
    name = name_regex.match(name_line)
    name = name.group(1)
    for line in gpl_file:
        raw = regex.match(line)
        if raw is not None:
            RGB  = raw.group()
            colors.append(RGB)

colors = [c.strip() for c in colors]
str_colors = list()
for c in colors:
    str_colors.append(c.split())

int_colors = str_colors_to_int(str_colors)
float_colors = list_int_to_float(int_colors)

hsv_colors = list_rgb_to_hsv(float_colors)
im_hsv = Image.new('HSV',(16,16))
im_hsv.putdata(hsv_colors)
im_hsv.show()
# SORTING{{{
partition_start = 0
partition_end = 128
sorted_int_colors = sorted(int_colors[partition_start:partition_end],key=lambda
        x:x[0],reverse=True) +  int_colors[partition_end + 1:]
sorted_int_tup = []
# }}}
# IMAGE LIBRARY IMAGE{{{
for c in sorted_int_colors:
    sorted_int_tup.append(tuple(c))
img = Image.new('RGB',(16,16))
#
img.putdata(sorted_int_tup)
#
img = img.resize((256,256),resample=4)
img.show()# }}}
# NP ARRAY IMAGE {{{
im_array = np.array(int_colors)
image = list()

for row in im_array:
    image.append(np.array(row))
im_rows = []
im_row = []
count = 0

for item in image:
    if count < 16:
        im_row.append([[item[0]],[item[1]],[item[2]]])
        count = count + 1
    else:
        im_rows.append(np.asarray(im_row))
        count = 0
        im_row = []
        # }}}
#  image = np.block(np.asarray(im_rows))
#  image = np.squeeze(image)
#  im = Image.fromarray(image, mode='RGB')
#  print(im.getpixel((15,7)))
#  print(image)
#  plt.imshow(image)
#  plt.show()
#    }}}



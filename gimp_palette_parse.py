# GIMP_PALETTE_PARSER.PY
# IMPORT THIS MODULE TO USE FUNCTIONS IN MAIN FILE 
import re
import PIL
from PIL import Image,ImageColor,ImagePalette
import colorsys 
# FUNCTION DEFS{{{

def list_int_to_float(list_in):
    list_out = []
    for tup in list_in:
        temp = ()
        for num in tup:
           temp = temp + (float(num/255),)
        list_out.append(temp)
    return list_out

def list_float_to_int(list_in):
    list_out = []
    for tup in list_in:
        temp = ()
        for num in tup:
            temp = temp + (int(num*255),)
        list_out.append(temp)
    return list_out


def str_colors_to_int(str_colors):
       int_colors = list()
       for c in str_colors:
           temp = []
           for val in c:
               temp.insert(0,int(val))
           int_colors.append(tuple(temp))
       return int_colors

def list_rgb_to_hsv(rgb_float_colors):
    hsv_colors = []
    for i in rgb_float_colors:
        hsv_colors.append(tuple(colorsys.rgb_to_hsv(i[0],i[1],i[2])))
    for tup in hsv_colors:
        count = 0
        temp = []
        for num in tup:
            temp.append(int(num*255))
            count = count + 1
        tup = tuple(temp)
    return hsv_colors

def rgb_sort(data,channel,ascending,partition_slice):
    if channel == 'r' or channel == 0:
        data_out = sorted(data[partition_slice[0]:partition_slice[1]], key=lambda
                x:x[0],reverse=ascending)
    elif channel == 'g' or channel == 1:
        data_out = sorted(data[partition_slice[0]:partition_slice[1]], key=lambda
                x:x[1],reverse=ascending)
    elif channel == 'b' or channel == 2:
        data_out = sorted(data[partition_slice[0]:partition_slice[1]], key=lambda
                x:x[2],reverse=ascending)

    if (partition_slice[1] - partition_slice[0]) < len(data):
        data_out = data[0:partition_slice[0]] + data_out + data[partition_slice[1]:len(data)]

    return data_out
# }}}
# CLASS DEFS {{{
class Colors:
    def __init__(self,file_path):
        self.file_path = file_path
        self.str_colors, self.palette = self.__parse_raw(file_path)
        self.int_colors = str_colors_to_int(self.str_colors)
        self.float_colors = list_int_to_float(self.int_colors)
        self.hsv_colors = list_rgb_to_hsv(self.float_colors)


    def __parse_raw(self,file_path): 
        regex = re.compile(r'^\s*(?P<R>\d*)\s*(?P<G>\d*)\s*(?P<B>\d*)')
        colors = []
        with open(file_path) as color_file:
            for line in color_file:
                raw = regex.match(line)
                if raw is not None:
                    R = raw.group('R')
                    G = raw.group('G')
                    B = raw.group('B')
                    if (R != '') and (G != '') and (B != ''):
                        R = int(R)
                        G = int(G)
                        B = int(B)
                        rgb = [R,G,B]
                        rgb_str = []
                        for item in rgb:
                            if item < 16:
                                item = '0'+hex(item)[2:]
                            else:
                                item = hex(item)[2:]
                            rgb_str.append(item)
                        rgb_str = '#' + ''.join(rgb_str)
                        colors.append(ImageColor.getrgb(rgb_str))
            pal = PIL.ImagePalette.ImagePalette(mode='RGB',palette=None, size=0)
        for c in colors:
            pal.getcolor(c)
        
        return colors, pal

    def color_print(self, color_model):
        #  0 = int_colors
        #  1 = float_colors
        #  2 = hsv_colors
        #  3 = str_colors
        if color_model == 0:
            print(self.int_colors)
        elif color_model == 1:
            print(self.float_colors)
        elif color_model == 2:
            print(self.hsv_colors)
        elif color_model == 3:
            print(self.str_colors)
   # }}}

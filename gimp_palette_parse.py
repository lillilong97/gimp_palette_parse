# GIMP_PALETTE_PARSER.PY
# IMPORT THIS MODULE TO USE FUNCTIONS IN MAIN FILE 
import re
import colorsys 
# FUNCTION DEFS{{{
def int_to_float(int_in):
    return(float(int_in/255))

def float_to_int(float_in):
    return(int(float_in*255))

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
               temp.append(int(val))
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
# }}}
# CLASS DEFS {{{
class Colors:
    def __init__(self,file_path):
        self.file_path = file_path
        self.str_colors = self.__parse_raw(file_path)
        self.int_colors = str_colors_to_int(self.str_colors)
        self.float_colors = list_int_to_float(self.int_colors)
        self.hsv_colors = list_rgb_to_hsv(self.float_colors)


    def __parse_raw(self,file_path): 
        colors = list()
        regex = re.compile(r'^\s*\d*\s*\d*\s*\d')
        name_regex = re.compile(r'Name: (.*)')
        with open(file_path) as gpl_file:
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
        return str_colors

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

# GIMP_PALETTE_PARSER.PY
# IMPORT THIS MODULE TO USE FUNCTIONS IN MAIN FILE

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



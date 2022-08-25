# gimp_palette_sort

this package is intended to parse and sort gimp palettes (filetype: .GPL)

import gimp_palette_parser as [whatever you want tbh]

# FLOAT_TO_INT
input: float_in (float)
output: float_in*255 casted to int
description: called inside list_int_to_float, 
converts normalized float values of colors to an integer between 0 and 255.
useful for moving between RGB and other color spaces. 

def float_to_int(float_in):
    return int(float*255)

[I'll finish documenting these later]

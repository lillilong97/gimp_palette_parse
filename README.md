 # gimp_palette_sort

this package is intended to parse and sort gimp palettes (filetype: .GPL)

import gimp_palette_parser as [whatever you want tbh]

## float_to_int
### input: 
``float_in`` (float)
    
### output: 
``int(float_in*255)`` (int) 

_input value multiplied by 255, cast to int_
    
### description: 
called inside ``list_int_to_float``, 
converts normalized float values of colors to an integer between 0 and 255.
useful for moving between RGB and other color spaces. 
    
### code: 
        def float_to_int(float_in):
            return int(float*255)

[I'll finish documenting these later]

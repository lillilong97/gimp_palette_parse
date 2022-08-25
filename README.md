 # gimp_palette_parse

this package is intended to parse and sort gimp palettes (filetype: .GPL)

import gimp_palette_parser as [whatever you want tbh]

## float_to_int<!--{{{-->
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
<!--}}}-->

## int_to_float<!--{{{-->
### input:
``int_in`` (int)

### output: 
``float(int_in/255)`` (float)
_input value divided by 255, cast to float_

### description:
called inside ``list_float_to_int``,
takes int value between 0 and 255 and converts it to a normalized float value
between 0 and 1.

### code
    def int_to_float(int_in):
        return float(int_in/255)
<!--}}}-->

## list_float_to_int<!--{{{-->

### input: 
``list_in`` (list)
_list of floats between 0 and 1_

### output:
``int_list_out`` (list)
_list of ints between 0 and 255_

### description:
takes a list of normalized float values between 0 and 1 and returns the scaled
values as integers between 0 and 255

### code: 
    def list_float_to_int(list_in):
        int_list_out = []
        for item in list_in:
            if type(item) is list:
                list_float_to_int(item)
            elif type(item) is float:
                int_list_out.append(float_to_int(item))
        return int_list_out
<!--}}}-->

## list_int_to_float<!--{{{-->

### input: 
``list_in`` (list)
_list of integers between 0 and 255_

### output: 
``list_out`` (list)
_list of normalized float values between 0 and 1_

### description:
takes a list of integers between 0 and 255 and returns a list of the converted
normalized float values between 0 and 1

### code:
    def list_int_to_float(list_in):
        float_list_out = []
        for item in list_in:
            if type(item) is list:
                list_int_to_float(item)
            elif type(item) is int:
               float_list_out.append(int_to_float(item))
        return float_list_out
<!--}}}-->

## str_colors_to_int<!--{{{-->

### input: 
``str_colors`` (list)
_list of values between 0 and 255 parsed from the .gpl file as strings_

### output:
``int_colors`` (list)
_list of integer values between 0 and 255 converted from the given string
values_

### description:
takes a list of string characters representing integers between 0 and 255 and
converts them to a list of integer values.
this is used to convert the data parsed from the .gpl file directly into usable
RGB data. 

### code:
    def str_colors_to_int(str_colors):
           int_colors = list()
           for c in str_colors:
               temp = []
               for val in c:
                   temp.append(int(val))
               int_colors.append(tuple(temp))
           return int_colors

<!--}}}-->

## list_rgb_to_hsv

### input: 
``rgb_float_colors`` (list) 
_list of float values between 0 and 1 that represent normalized RGB values_

### output:
``hsv_colors`` (list)
<!--uhhhh, is this returning integers or floats? will have to update later  -->

### description:


### code:
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




[I'll finish documenting these later]

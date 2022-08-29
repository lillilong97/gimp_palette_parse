from PIL import Image,ImageColor
import re

regex = re.compile(r'^\s*(?P<R>\d*)\s*(?P<G>\d*)\s*(?P<B>\d*)')
colors = []

with open('../Bears.gpl') as color_file:
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
                print(rgb_str)
                colors.append(ImageColor.getrgb(rgb_str))

print(colors)

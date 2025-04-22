from color import start_r, start_g, start_b,end_r, end_g, end_b
from color import coloredstring

invertbar = False

def line(lenght=11, base="-"):
    output=""
    for i in range(lenght):
        output = output + base
    return output


def processbar(currentprocess, maxprocess, lenght=10):
    currentprocess, maxprocess = int(currentprocess), int(maxprocess)
    currentprocess, maxprocess = int(currentprocess / maxprocess * lenght), int(lenght)
    output = "[ "
    full = "■"
    empty = "-"
    for i in range(currentprocess):
        factor = i / maxprocess
        if not invertbar:
            r = int(end_r + (start_r - end_r) * factor)
            g = int(end_g + (start_g - end_g) * factor)
            b = int(end_b + (start_b - end_b) * factor)
        else:
            r = int(start_r + (end_r - start_r) * factor)
            g = int(start_g + (end_g - start_g) * factor)
            b = int(start_b + (end_b - start_b) * factor)
        output = output + coloredstring(full, r, g, b)
    for i in range(maxprocess-currentprocess):
        output = output + empty
    return output + " ]"
import color
from color import start_r, start_g, start_b,end_r, end_g, end_b

logo = [
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    "                                   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   ",
    " llllllllllllll   llllllllllllll   "
]

def getlogo(line):
    #gradient
    max_lines = 15
    diffactor = line / max_lines
    r = int(start_r + (end_r - start_r) * diffactor)
    g = int(start_g + (end_g - start_g) * diffactor)
    b = int(start_b + (end_b - start_b) * diffactor)
    return color.coloredstring(logo[line], r, g, b)
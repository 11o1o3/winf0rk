from color import coloredblock as cb


# number of blanks to represent one color
blanknum = 3

# color palette
colors_dark = ((0, 0, 0), (220, 80, 230), (130, 40, 235), (130, 110, 230), (120, 100, 230), (40, 130, 230), (40, 170, 240), (220, 220, 220))
colors_light = ((135, 135, 135), (240, 170, 240), (200, 150, 200), (200, 190, 250), (190, 180, 240), (150, 200, 250), (150, 215, 250), (240, 240, 240))

colorbar_dark, colorbar_light = "", ""
for i in colors_dark:
    colorbar_dark = colorbar_dark + cb(i[0], i[1], i[2], blanknum)
for i in colors_light:
    colorbar_light = colorbar_light + cb(i[0], i[1], i[2], blanknum)

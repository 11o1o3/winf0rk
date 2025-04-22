import jumpingspider as js

start_r, start_g, start_b = 0, 100, 255  # Blue
end_r, end_g, end_b = 150, 0, 200  # Purple

def coloredstring(text, r, g, b):
    return js.rgb_color_text(text, r, g, b)

def coloredblock(r, g, b, amount=1):
    output=""
    for i in range(amount):
        output = output + " "
    return js.rgb_bg_text(output, r, g, b)
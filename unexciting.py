from colormath.color_objects import HSVColor, sRGBColor
from colormath.color_conversions import convert_color

# The color numbers are:
#   0: black
#   1: red
#   2: green
#   3: yellow
#   4: blue
#   5: magenta
#   6: cyan
#   7: white
#       blk  red  grn  ylw  blu  mag  cya  wht
hues = [170,   0, 105,  58, 220, 295, 175, 195]
sats = [ 25,  80,  80,  80,  60,  80,  80,  10]
vals = [ 12,  80,  70,  80,  95,  80,  80,  87]

cursor_color = HSVColor(85, .95, 1)

colors = []

for i in range(8):
    color = HSVColor(hues[i], sats[i] / 100, vals[i] / 100)
    colors.append(color)

for i in range(8):
    dark = colors[i]
    light = HSVColor(dark.hsv_h, min(1, dark.hsv_s * 0.8), min(1, dark.hsv_v * 3))
    colors.append(light)

rgb_colors = []

for i in range(16):
    rgb = convert_color(colors[i], sRGBColor)
    rgb_colors.append(rgb)

rgb_colors.append(convert_color(cursor_color, sRGBColor))

def to_keyvalue(rgb, specials={}, normalFormat="*.color{0}: {1}\n", specialFormat="*.{0}: {1}\n"):
    result = ""
    for name, idx in specials.items():
        result += specialFormat.format(name, rgb[idx].get_rgb_hex())
    for idx in range(16):
        result += normalFormat.format(idx, rgb[idx].get_rgb_hex())
    return result

def to_xresources(rgb):
    return to_keyvalue(rgb, specials={
        "cursorColor": 16,
        "foreground": 7,
        "background": 0,
    })

def to_termux(rgb):
    return to_keyvalue(rgb, specials={
            "cursor": 16,
            "foreground": 7,
            "background": 0,
        },
        normalFormat="color{0}={1}\n",
        specialFormat="{0}={1}\n",
    )

def srgb2dword(color):
    tup = color.get_upscaled_value_tuple()
    return "dword:{0:08x}".format(tup[0] + (tup[1] << 8) + (tup[2] << 16))

def to_windows_console(rgb):
    mapping = [0, 4, 2, 6, 1, 5, 3, 7, 8, 12, 10, 14, 9, 13, 11, 15]
    result = "Windows Registry Editor Version 5.00\r\n[HKEY_CURRENT_USER\\Console]\r\n"
    for idx in range(16):
        result += '"ColorTable{0:02d}"={1}\r\n'.format(idx, srgb2dword(rgb[mapping[idx]]))
    result += '"CursorColor"={0}\r\n'.format(srgb2dword(rgb[16]))
    result += '"ScreenColors"=dword:00000007\r\n"PopupColors=dword:00000083\r\n'
    return result

with open("unexciting.Xresources", "w") as file:
    print(to_xresources(rgb_colors), file=file, end="")

with open("unexciting.termux.colors.properties", "w") as file:
    print(to_termux(rgb_colors), file=file, end="")

with open("unexciting.windows-console.reg", "w") as file:
    print(to_windows_console(rgb_colors), file=file, end="")

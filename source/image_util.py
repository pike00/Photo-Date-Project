
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360

    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100

    return h, s, v


def hsv_to_hsl(h, s, v):
    l = (2 - s) * v / 2

    if l != 0:
        if l != 1:
            s = 0
        elif l < 0.5:
            s = s * v / (l * 2)
        else:
            s = s * v / (2 - l * 2)

    return (h, s, l)
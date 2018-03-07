
from PIL import Image


# Function to covert rgb to hsv
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v


def analyse_image(file_name):
    img_file = Image.open(file_name)
    img = img_file.load()

    # Construct a blank matrix representing the pixels in the image
    [xs, ys] = img_file.size

    greens = []
    # Examine each pixel in the image file
    for x in range(0, xs):
        for y in range(0, ys):
            # ( )  Get the RGB color of the pixel
            [r, g, b, o] = img[x, y]
            h = rgb2hsv(r, g, b)[0]
            if 70 <= h <= 140:
                greens.append([x, y, h])

    total_pixels = xs * ys    
    green_pixels = len(greens)
    percent_green = green_pixels / total_pixels * 100
    return percent_green, total_pixels, green_pixels


print(analyse_image('source/green.png')[0])

from __future__ import print_function
import argparse
import PPM.PPM_P6 as ppm
import array

def RGB(**kwargs):
    RGB = {
        'R': 3*((kwargs['y'])*kwargs['width']+kwargs['x']),
        'G': 3*((kwargs['y'])*kwargs['width']+kwargs['x']) + 1,
        'B': 3*((kwargs['y'])*kwargs['width']+kwargs['x']) + 2,
    }
    return RGB

def draw(args):
    infile = args["input"]
    outfile = args["output"]
    (start_x, start_y) = args["location"]
    (width, height) = args["size"]
    color = args["color"]
    maxval = 255

    ppm_p6 = ppm.PPM_P6()
    ppm_p6.width = width
    ppm_p6.height = height
    ppm_p6.maxval = maxval

    (width, height, maxval, bitmap) = ppm_p6.read(infile)
    image = array.array('B', bitmap)
    for x in range(0, width):
        for y in range(0, height):
            x = x + start_x
            y = y + start_y
            image[RGB(width=width, x=x, y=y)['R']] = color[0]
            image[RGB(width=width, x=x, y=y)['G']] = color[1]
            image[RGB(width=width, x=x, y=y)['B']] = color[2]

    ppm_p6.write(width, height, maxval, image, outfile)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to the input image")
ap.add_argument("-o", "--output", required=True, help="Path to the output image")
ap.add_argument("-l", "--location", type=int, nargs='+', default=[0, 0], help="starting point")
ap.add_argument("-s", "--size", type=int, nargs='+', default=[50, 30], help="Size of the rectangle image")
ap.add_argument("-c", "--color", type=int, nargs='+', default=[0, 0, 0], help="color of the rectangle image")

args = vars(ap.parse_args())

draw(args)
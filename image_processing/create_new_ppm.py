from __future__ import print_function
import argparse
import PPM.PPM_P6 as ppm

def create_ppm(args):
    outfile = args["output"]
    (width, height) = args["size"]
    color = args["color"]
    colors = color * width * height
    maxval = 255

    ppm_p6 = ppm.PPM_P6()
    ppm_p6.width = width
    ppm_p6.height = height
    ppm_p6.maxval = maxval

    ppm_p6.write(width, height, maxval, colors, outfile)

ap = argparse.ArgumentParser()

ap.add_argument("-o", "--output", required = True, help="Path to the output image")
ap.add_argument("-s", "--size", type=int, nargs='+', default=[50,30], help="Size of the output image")
ap.add_argument("-c", "--color", type=int, nargs='+', default=[255, 255, 255], help="Color of the output image")

args = vars(ap.parse_args())

create_ppm(args)
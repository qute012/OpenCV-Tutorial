from __future__ import print_function
import argparse
import PPM.PPM_P6 as ppm
import array


ap = argparse.ArgumentParser()
#옵션들
ap.add_argument("-i", "--input", required = True, help = "Path to the input image")
ap.add_argument("-o", "--output", required = True, help ="Path to the output image")
ap.add_argument("-p", "--position", type = int, nargs = '+', default = [0,0], help = "position of the rectangle image")
ap.add_argument("-s", "--size", type = int, nargs = '+', default = [50, 50], help = "Size of the rectangle image")
ap.add_argument("-c", "--color", type = int, nargs = '+', default = [255, 0, 0], help = "color of the rectangle image")

args = vars(ap.parse_args())

infile = args["input"]
outfile = args["output"]
(width,height) = args["size"]
(xpos, ypos) = args["position"]

maxval = 255

color = args["color"]

ppm_p6 = ppm.PPM_P6()

ppm_p6.width = width
ppm_p6.height = height
ppm_p6.maxval = maxval

print(ppm_p6)

(Rwidth, Rheight, Rmaxval, Rbitmap) = ppm_p6.read(infile)
#
image = array.array('B', Rbitmap)
#index = 3* (y *width + x)

for x in range(0, width):
   for y in range(0, height):
      image[3*((y+ypos)*Rwidth+(x+xpos))+0] = color[0]
      image[3*((y+ypos)*Rwidth+(x+xpos))+1] = color[1]
      image[3*((y+ypos)*Rwidth+(x+xpos))+2] = color[2]

ppm_p6.write(Rwidth, Rheight, maxval, image, outfile)

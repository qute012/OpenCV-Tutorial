from __future__ import print_function
import argparse
import PPM.PPM_P6 as ppm

ap = argparse.ArgumentParser()

#옵션
ap.add_argument("-o", "--output", required = True, help = "Path to the output image")
ap.add_argument("-s", "--size", type = int, nargs = '+', default=[50,30], help = "Size of the output image")
ap.add_argument("-c", "--color", type = int, nargs = '+', default = [255,255,255], help = "Color of the output image")

args = vars(ap.parse_args())


outfile = args["output"]
(width, height) = args["size"]
maxval = 255

color = args["color"]
colors = color * width * height

ppm_p6 = ppm.PPM_P6()
#기본 생성자에 의해 width, height, maxval 이 모두 0으로 생성됨
ppm_p6.width = width
ppm_p6.height = height
ppm_p6.maxval = maxval
#ppm 헤더에 값을 지정해줌


print(ppm_p6)

ppm_p6.write(width, height, maxval, colors, outfile)
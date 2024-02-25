# Pillow for image reading
# numpy for computing
from PIL import Image
import numpy as np
import math
import sys, random, argparse


# these are two different scales, scale1 has 70 levels of brightness, whereas scale2 has 10 levels.
grayscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`"
grayscale2 = "@%#*+=-:."

# find the average value of the grayscale
def getAverageL(image):
    im = np.array(image)                    # convert the image into a numpy array
    w,h = im.shape                          # store into w and h the dimensions of the array.
    return np.average(im.reshape(w*h))      # flatten the array into one dimension

def convertImageToAscii(fileName, cols, scale, moreLevels):
    global grayscale1, grayscale2
    # find and process the image and convert to grayscale.
    image = Image.open('filler.jpg').convert('L')

    # find and store the dimensions of the image. ex: 1920 x 1080
    W, H = image.size[0], image.size[1]
    print("Input image dims: %d x %d" % (W,H))

    w = W/cols
    h = w/scale
    rows = int(H/h)
    print("cols: %d, rows: %d" % (cols,rows))
    print("tile dims: %d x %d" % (w,h))

    if cols > W or rows > H:
        print("Image is too small for specified column values")
        exit(0)

    aimg = []

    for j in range(rows):
        y1 = int (j*h)
        y2 = int ((j+1)*h)
        if j == rows-1:
            y2 = H
        aimg.append("")
        for i in range(cols):
            x1 = int (i*w)
            x2 = int((i+1)*w)
            if i == cols-1:
                x2 = W
    # crop the image and extract the specific tile
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            gsval = grayscale1[int((avg*69)/255)]
            #gsval = grayscale2[int((avg*9)/255)]
            aimg[j] += gsval                    # append the char into this image array
    
    return aimg

def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
 
    # parse args
    args = parser.parse_args()
   
    imgFile = args.imgFile
 
    # set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
 
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
 
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
 
    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = convertImageToAscii(imgFile, cols, scale, args.moreLevels)
 
    # open file
    f = open(outFile, 'w')
 
    # write to file
    for row in aimg:
        f.write(row + '\n')
 
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)
 
# call main
if __name__ == '__main__':
    main()
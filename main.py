# Pillow for image reading
# numpy for computing
from PIL import Image
from numpy import np

# these are two different scales, scale1 has 70 levels of brightness, whereas scale2 has 10 levels.
grayscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`"
grayscale2 = "@%#*+=-:."

# open the image file


# find and process the image and convert to grayscale.
image = Image.open('filler.jpg')
gray_img = image.convert('L')

# find and store the dimensions of the image. ex: 1920 x 1080
cols = 80
aspect_ratio = image.size[1]/image.size[0]  # height / width
W, H = image.size[0], image.size[1]
w = W/cols
h = w/aspect_ratio
rows = int(H/h)

# find the average value of the grayscale
def getAverageL(image):
    im = np.array(image)                    # convert the image into a numpy array
    w,h = im.shape                          # store into w and h the dimensions of the array.
    return np.average(im.reshape(w*h))      # flatten the array into one dimension

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
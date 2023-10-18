import urllib.request
from PIL import Image

# Original 512x512
urllib.request.urlretrieve('https://i.ibb.co/tMpTt08/image.png', "image.png")

# Cropped 64x64 for testing
# urllib.request.urlretrieve('https://i.ibb.co/Np0q8P2/image2.png', "image.png")

image = Image.open("image.png")
pixel_map = image.load()
width, height = image.size

ccfNum = 10
ccfRange = 10
ccfLoc = [0] * ccfNum
CO2 = [0] * ccfNum
pixel = [0] * width * height
array = [0] * width * height


def loadPixels():
    for i in range(width * height):
        loc = i % width, i // width
        temp = image.getpixel(loc)
        pixel[i] = temp[0]


def findLoc():
    for y in range(height):
        for x in range(width):
            array[x + y * width] = calc(x, y)
    maxVal = array.index(max(array))
    return maxVal


def calc(x, y):
    val = 0
    for yv in range(-ccfRange, ccfRange + 1):
        for xv in range(-ccfRange, ccfRange + 1):
            if (xv ** 2 + yv ** 2) ** 0.5 <= ccfRange and 0 <= x + xv < width and 0 <= y + yv < height:
                val += pixel[x + xv + (y + yv) * width]
    return val


def erase(val):
    x = val % width
    y = val // width
    for yv in range(-ccfRange, ccfRange + 1):
        for xv in range(-ccfRange, ccfRange + 1):
            if (xv ** 2 + yv ** 2) ** 0.5 <= ccfRange and 0 <= x + xv < width and 0 <= y + yv < height:
                pixel[x + xv + (y + yv) * width] = 0


def run():
    print("\nFinding locations for ", ccfNum, " CCFs with range of ", ccfRange, "px")
    print("Amount of CO2:", sum(pixel), "\n")
    for i in range(ccfNum):
        CO2[i] = sum(pixel)
        ccfLoc[i] = findLoc()
        print("Location for CCF no. ", i + 1, ": x", ccfLoc[i] % width, " y", ccfLoc[i] // width, sep='')
        erase(ccfLoc[i])
        print("Amount of CO2:", sum(pixel), end='')
        print(" (-", CO2[i] - sum(pixel), ")", sep='')
        print("Percentage removed: ", round(100 * (CO2[0] - sum(pixel)) / CO2[0], 2), "%", sep='', end='')
        print(" (+", round(100 * (CO2[i] - sum(pixel)) / CO2[0], 2), "%)\n", sep='')
    for i in range(ccfNum):
        print(";" if i > 0 else "", ccfLoc[i] % width, ",", ccfLoc[i] // width, sep='', end='')


loadPixels()
run()

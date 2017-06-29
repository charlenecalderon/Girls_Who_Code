from PIL import Image

#import image
myImage = Image.open("rtr.jpeg")
imageData = myImage.getdata()
pixelList = (imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]

    newRed = red*6
    if newRed > 255:
        newRed = 255

    

    newBlue = blue*7
    if newBlue > 255:
        newBlue = 255


    newGreen = green*7
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)


#add pixel to new pixel list
    newPixelList.append(p)

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()

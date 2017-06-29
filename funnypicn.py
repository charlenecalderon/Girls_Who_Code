from PIL import Image

#import image
myImage = Image.open("elephant2.jpg")
imageData = myImage.getdata()
pixelList = (imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]

    #find average of color values
    #average = int((red + blue + green)// 3)


    
    newRed = (255-red)
    if newRed > 255:
        newRed = 255

    

    newBlue = (255-blue)
    if newBlue > 255:
        newBlue = 255


    newGreen = (255-green)
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)

    
    #newRed = average
    #newBlue = average
    #newGreen = average


#add pixel to new pixel list
    newPixelList.append(p)

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
print(newRed)
print(newBlue)
print(newGreen)


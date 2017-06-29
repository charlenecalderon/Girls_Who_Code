from PIL import Image

#function

def blue22(pixel):
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]
    
    newRed = (red)
    if newRed > 255:
        newRed = 255

    newBlue = (blue)*2
    if newBlue > 255:
        newBlue = 255

    newGreen = (green)
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)
    newPixelList.append(p)

def red22(pixel):
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]
    
    newRed = (red)* 2
    if newRed > 255:
        newRed = 255

    newBlue = (blue)
    if newBlue > 255:
        newBlue = 255

    newGreen = (green)
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)
    newPixelList.append(p)
    
def bnw(pixel):
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]

    #find average of color values
    average = int((red + blue + green)// 3)


    
    newRed = average
    if newRed > 255:
        newRed = 255

    

    newBlue = average
    if newBlue > 255:
        newBlue = 255


    newGreen = average
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)

    
    newRed = average
    newBlue = average
    newGreen = average


#add pixel to new pixel list
    newPixelList.append(p)



#import image
myImage = Image.open("elephant2.jpg")
imageData = myImage.getdata()
pixelList = (imageData)

newPixelList = []

length = len(pixelList)
top = (length // 3)
middle = 2 * (length // 3)
bottom = (length)


counter = 0

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue =  pixel[2]

    if (counter < (length * 1//3)):
        red22(pixel)
    elif (counter < (2 * (length //3))):
        bnw(pixel)
        
    else:
        blue22(pixel)
    counter = counter + 1
        
  


#add pixel to new pixel list
    #newPixelList.append(p)

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
print(newRed)
print(newBlue)
print(newGreen)

from PIL import Image

def colorpick(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    intensity = (red + green + blue)
    darkblue = (0,51,76)
    red1 = (217,26,33)
    lightblue = (112,150,158)
    yellow = (252,227,166)



    if(intensity < 182):
        newPixelList.append(darkblue)
    if(intensity >= 182) and (intensity <364):
        newPixelList.append(red1)
    if(intensity >= 364) and (intensity <546):
        newPixelList.append(lightblue)
    if(intensity >= 546):
        newPixelList.append(yellow)
#running code
    
#import image
myImage = Image.open("abi.jpg")
imageData = myImage.getdata()
pixelList = (imageData)

newPixelList = []


#pixel manipulation
for x in pixelList:
    

    colorpick(x)

    
        
        
  


#add pixel to new pixel list
    #newPixelList.append(p)

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()


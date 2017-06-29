from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
def drawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        charlene.forward(50)
        charlene.right(angle)
        drawnSides+=1

another = True

charlene = Turtle()
charlene.turtlesize(2,2)
charlene.pensize(5)
charlene.pendown()

while another == True:
    print ("How many sides do you want your shape to have?")
    numSides = int(input())
    print ("What color do you want your shape to be?")
    chosenColor = input()
    drawShape(charlene,numSides,chosenColor)
    print("Do you want to draw another shape?")
    answer = input()
    if(answer=="no"):
        another = False


#charlene.pencolor("blue")
#drawShape(charlene,3)

#charlene.pencolor("yellow")
#drawShape(charlene,8)

print("Thank You")
    
exitonclick()



# Close window on click.
exitonclick()


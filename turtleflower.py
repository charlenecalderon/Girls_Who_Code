from turtle import *
import math

setup(800,800)

def DrawFlower(turtle,color,size,circle):
    turtle.pencolor(color)
    turtle.circle(size)

    for i in range (input):
        turtle.right(30)


flower =Turtle()
flower.pendown()
#DrawFlower(flower,"black",50)
#flower.right(40)
#DrawFlower(flower,"black",50)




print("How many pedals do you want your flower to have?")
pedals = int(input())
for i in range(pedals):
    flower.right(30)

print("What size do you want your pedals?")
size = int(input())

DrawFlower(flower,color,size,circle)
    
exitonclick()

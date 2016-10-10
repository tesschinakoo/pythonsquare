# THIS SHOULD ALWAYS BE YOUR FIRST LINE
from Myro import *
init("sim") #if your simulator is not running

def squareside(): #function for first three sides of square
    forward(2,2)
    wait(.5)
    turnBy(90)
  
def triangleside(): #function for first two sides of triangle
    penDown()
    forward(1,2)
    penUp()
    wait(.1)
    turnBy(120)

#SQUARE BEGINS
penDown()
squareside()
squareside()
squareside()
forward(2,2)
penUp()

#MOVE TO START LOCATION OF TRIANGLE
forward(1,1)

#TRIANGLE BEGINS
triangleside()
triangleside()
penDown()
forward(1,2.1)
penUp()
wait(.5)

#MOVE TO STARTING LOCATON OF LETTER T
forward(2,1)
turnLeft(1,1)
forward(2,1)

#LETTER T BEGINS
penDown()
forward(2,1)
penUp()
backward(1,1)
turnBy(90)
penDown()
forward(2,1)
penUp()
wait(.5)

forward(2,.5)
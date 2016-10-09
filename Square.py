# THIS SHOULD ALWAYS BE YOUR FIRST LINE
from Myro import *
init("sim") #if your simulator is not running

#SQUARE BEGINS
penDown()
forward(2,2)
wait(.5)
turnLeft(1,1)
turnLeft(1,1)
turnLeft(1,.472)
wait(.1)
forward(2,2)
wait(.5)
turnLeft(1,1)
turnLeft(1,1)
turnLeft(1,.473)
wait(.1)
forward(2,2)
wait(.5)
turnLeft(1,1)
turnLeft(1,1)
turnLeft(1,.472)
wait(.1)
forward(2,2)
wait(.1)
penUp()

#MOVE TO START LOCATION OF TRIANGLE
forward(1,1)

#TRIANGLE BEGINS
penDown()
forward(1,2)
penUp()
wait(.1)
turnLeft(3,1)
wait(.1)
penDown()
forward(1,2)
penUp()
wait(.1)
turnLeft(3.5,1)
wait(.3)
penDown()
forward(1.2,2)
penUp()

#MOVE TO STARTING LOCATON OF LETTER T
forward(2,1)
turnLeft(1,1)
forward(2,1)

#LETTER T BEGINS
penDown()
forward(2,1)
backward(1,1)
turnLeft(2.48,1)
forward(2,1)
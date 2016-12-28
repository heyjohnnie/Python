import turtle
import sys

#Defining the int input method, if the user types a non numerical value,
#the error will be hanlded without ending the program.
def userInputAsInt():
    flag = False
    valueAsStr = ""
    valueAsInt = 0
    while flag == False:
        valueAsStr = input("Type the value: ")
        try:
            valueAsInt = int(valueAsStr)
            flag = True
        except:
            error = sys.exc_info()[0]
            print(error)
            print("Invalid input, use numeric values.")
    return valueAsInt

#The geometrical figure is defined as an object.
class parallelogram(object):
    def __init__(self, side, lenght):
        self.side = side
        self.length = lenght

    def geometry(self):
        for steps in range(self.side):
            turtle.forward(self.length)
            turtle.right(360/self.side)

print("Please, enter the number of sides: ")
numOfSides = userInputAsInt()
print("Please, enter the side lenght: ")
sideLenght = userInputAsInt()

userGeometry = parallelogram(numOfSides, sideLenght)
userGeometry.geometry()

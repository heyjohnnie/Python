import turtle
import sys

#Defining the int input method, if the user types a non numerical value,
#the error will be hanlded without ending the program.
class userInput:

    def __init__(self):
        self.valueAsStr = ""
        self.valueAsInt = 0

    def inputAsInt(self):
        while 1:
            valueAsStr = input("Enter the value: ")
            try:
                valueAsInt = int(valueAsStr)
                break
            except:
                error = sys.exc_info()[0]
                print(error)
                print("Invalid input, use numerical values.")
        self.valueAsStr = valueAsStr
        self.valueAsInt = valueAsInt
        return valueAsInt

#def userInputAsInt():
#    flag = False
#    valueAsStr = ""
#    valueAsInt = 0
#    while flag == False:
#        valueAsStr = input("Type the value: ")
#        try:
#            valueAsInt = int(valueAsStr)
#            flag = True
#        except:
#            error = sys.exc_info()[0]
#            print(error)
#            print("Invalid input, use numeric values.")
#    return valueAsInt

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
numOfSides = userInput()
sidesInGeo = numOfSides.inputAsInt()
print("Please, enter the side lenght: ")
sideLenght = userInput()
lengthInGeo = sideLenght.inputAsInt()

userGeometry = parallelogram(sidesInGeo, lengthInGeo)
userGeometry.geometry()

import turtle
import sys

#First aproach to user input using methods.
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

class userInput:
    #Defining the input as an object, if the user types a non numerical value,
    #the error will be hanlded without ending the program.
    def __init__(self):
        self._valueAsStr = ""
        self._valueAsInt = 0

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
        self._valueAsStr = valueAsStr
        self._valueAsInt = valueAsInt
        return valueAsInt

#The geometrical figure is defined as an object.
class parallelogram:
    def __init__(self, side, lenght):
        self._side = side
        self._length = lenght

    def geometry(self):
        for steps in range(self._side):
            turtle.forward(self._length)
            turtle.right(360/self._side)

#The program asks for the number of sides, the numOfSides instance is created.
print("Please, enter the number of sides: ")
numOfSides = userInput()
#The sidesInGeo is the int parameter that the geometry() method will use.
sidesInGeo = numOfSides.inputAsInt()
print("Please, enter the side lenght: ")
sideLenght = userInput()
lenghtInGeo = sideLenght.inputAsInt()

#The userGeometry instance is created, using sidesInGeo and lenghtInGeo as parameters.
#Then, the object is drawn using the geometry() method
userGeometry = parallelogram(sidesInGeo, lenghtInGeo)
userGeometry.geometry()

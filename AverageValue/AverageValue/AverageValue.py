HOTKEY = "DONE"

#Function to create a user defined list of numbers, a previous variable HOTKEY is required before using the code
def userListAsFloat ():
    import sys
    userInput = " "
    values = []
    while userInput != HOTKEY:
        userInput = input("Enter the desired value, if none required, type " + HOTKEY + ": ").upper()
         #If a non number value is typed, the except will handle the error and will allow the loop to continue
        try:
            if userInput != HOTKEY:
                inputAsFloat = float(userInput)
                values.append(inputAsFloat)
        except:
            error = sys.exc_info()[0]
            print(error)
            print("Invalid input, use only numeric values or " + HOTKEY)
    return values

#Function defined as sigmaSummation for math greek symbol, adds each numeric value of a list and returns the total amount
def sigmaSummation (range):
    total = 0
    for number in range:
        total += number
    return total

listOfNumbers = userListAsFloat()
totalValueOfList = sigmaSummation(listOfNumbers)

averageValue = totalValueOfList / len(listOfNumbers)
print("The average value is " + str(averageValue))

#Convert str list into float and loop to add each individual value into the total
#valuesAsFloat = [float(number) for number in values]
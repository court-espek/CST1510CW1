import math
import re

def wholeNumberSection(binaryNum):
    '''Returns the conversion from binary to decimal of the separated whole number section'''
    convertedValue = 0
    for i in range(len(str(binaryNum))):
        rem = binaryNum%10 # gets the LSB
        binaryNum //= 10 # removes the LSB
        convertedValue += rem*(math.pow(2,i)) # raises the value to 2^index
    return convertedValue

def fractionSection(binaryNum):
    '''Returns the conversion from binary to decimal of the separated fraction section'''
    convertedValue = 0
    for j in range(len(str(binaryNum))):
        convertedValue += int(binaryNum[j]) * (math.pow(2,-(j+1))) # raises the value to 2^-index
    return convertedValue

def binaryToDecimal(binaryString):
    '''Returns the conversion of an entire binary number by input of a string of binary numbers'''
    #Checks if the input has a decimal point
    if "." in binaryString:
        #splits the input into two parts - whole and fractional
        numParts = re.split(r'\.', binaryString)

        wholeValue = wholeNumberSection(int(numParts[0]))
        fractionValue = fractionSection(numParts[1])
        
        return wholeValue + fractionValue
    
    else: #if inputted number has no decimal point
        return wholeNumberSection(int(binaryString))
        
#user input and verification of digits
numString = input("Enter binary number to convert to decimal:\t")
if re.fullmatch(r'[01.]+',numString):
    numDecimal = binaryToDecimal(numString)
    print(f"Binary Number:\t{numString}\nDecimal Number:\t{numDecimal}") 
else:
    print("Invalid binary number input.")
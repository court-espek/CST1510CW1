import random

#function to check if the entered digit is valid using try and except
def checkInput():
    while True:
        inputString = input("Answer: ")
        try:
            return float(inputString)
        except ValueError:
            print("Please enter a numeric answer: ")

#function for addition option
def addition():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} + {number2}?")
    answer = checkInput() #user input is done through the checkInput function
    return answer == (number1+number2)

#function for subtraction operation
def subtraction():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} - {number2}?")
    answer = checkInput()
    return answer == (number1-number2)

#function for the multiplication operation
def multiplication():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} * {number2}?")
    answer = checkInput()
    return answer == (number1*number2)

#function for the division operation
def division():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} / {number2}? (Correct to 2 decimal places)")
    if number2 != 0: #checks if the number is being divided by 0
        answer = checkInput()
        return answer == (round((number1/number2),2))
    else: #user is not penalized for possibly dividing by 0
        print("Division by Zero detected! Answer will be undefined, score will not be deducted.")
        return True
    
#function for the exponent operation
def exponent():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} ^ {number2}?")
    answer = checkInput()
    return answer == (number1**number2)

#function for the remainder operation
def remainder():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print(f"What is {number1} % {number2}?")
    answer = checkInput()
    return answer == (number1%number2)

#variable initialization where the score and questions are 0 at the start
score = 0
totalQuestions = 0
#while loop to continue runnning until user decides otherwise
while True:
    #input is set to lowercase should the user used mixed-case letters
    operation = input("Operations:\n Addition\t| Subtraction\t| Multiplication\t| Division\t| Exponent\t| Remainder.\nEnter your choice: ").lower()

    #if statements to separate each operation
    if operation.lower() == "addition":
        totalQuestions += 1
        if addition() == True: #if the inputted answer matches calculated answer
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "subtraction":
        totalQuestions += 1
        if subtraction() == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "multiplication":
        totalQuestions += 1
        if multiplication() == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "division":
        totalQuestions += 1
        if division() == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "exponent":
        totalQuestions += 1
        if exponent() == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "remainder":
        totalQuestions += 1
        if remainder() == True:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    elif operation.lower() == "exit":
        print(f"Final score: {score}/{totalQuestions}")#prints the users score
        break
    else: #in the case the user does not enter an expected output
        print("Invalid input!")
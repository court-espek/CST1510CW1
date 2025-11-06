import random

#function to check if the entered digit is valid using try and except
def checkInput():
    while True:
        inputString = input("Answer: ")
        try:
            return float(inputString)
        except ValueError:
            print("Please enter a numeric answer: ")

#dictionary of operations - where every key is an operation and the values are lambda functions
operations = {
    "addition": lambda number1, number2: number1 + number2,
    "subtraction": lambda number1, number2: number1 - number2,
    "multiplication": lambda number1, number2: number1 * number2,
    "division": lambda number1, number2: round((number1 / number2),2),
    "exponent": lambda number1, number2: number1 ** number2,
    "remainder": lambda number1, number2: number1 % number2
}

#variable initialization where the score and questions are 0 at the start
score = 0
totalQuestions = 0
#while loop to continue runnning until user decides otherwise
while True:
    #input is set to lowercase should the user used mixed-case letters
    operation = input("Operations:\n Addition\t| Subtraction\t| Multiplication\t| Division\t| Exponent\t| Remainder.\nEnter your choice: ").lower()
    #variable initialization of randomly generated single-digit numbers
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    #if statements to separate each operation
    #operation for addition
    if operation.lower() == "addition":
        totalQuestions += 1
        correctAnswer = operations["addition"](number1,number2)
        print(f"What is {number1} + {number2}?")
        userAnswer = checkInput() #all numerical inputs are run through this function
        if userAnswer == correctAnswer: #if the inputted answer matches calculated answer
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    #operation for subtraction
    elif operation.lower() == "subtraction":
        totalQuestions += 1
        correctAnswer = operations["subtraction"](number1,number2)
        print(f"What is {number1} - {number2}?")
        userAnswer = checkInput()
        if userAnswer == correctAnswer: 
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    #operation for multiplication
    elif operation.lower() == "multiplication":
        totalQuestions += 1
        correctAnswer = operations["multiplication"](number1,number2)
        print(f"What is {number1} * {number2}?")
        userAnswer = checkInput()
        if userAnswer == correctAnswer: 
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    #operation for division
    elif operation.lower() == "division":
        totalQuestions += 1
        if number2 != 0:
            correctAnswer = operations["division"](number1,number2)
            print(f"What is {number1} / {number2}? (Correct to two decimal places)")
            userAnswer = checkInput()
            if userAnswer == correctAnswer: 
                score += 1
                print("Correct!")
            else:
                print("Wrong!")
        else: #if the second number is 0, the user will not be penalized by a zero division
            print(f"What is {number1} / {number2}?\n Division by Zero detected! Answer is undefined, score is unaffected.")
            totalQuestions -=1
            continue

    #operation for exponents
    elif operation.lower() == "exponent":
        totalQuestions += 1
        correctAnswer = operations["exponent"](number1,number2)
        print(f"What is {number1} ^ {number2}?")
        userAnswer = checkInput()
        if userAnswer == correctAnswer: 
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    #operation for remainders
    elif operation.lower() == "remainder":
        totalQuestions += 1
        correctAnswer = operations["remainder"](number1,number2)
        print(f"What is {number1} % {number2}?")
        userAnswer = checkInput()
        if userAnswer == correctAnswer: 
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    
    elif operation.lower() == "exit":
        print(f"Final score: {score}/{totalQuestions}")#prints the users score
        break
    else: #in the case the user does not enter an expected output
        print("Invalid input!")
#variable initialization and user input
listStudents = []
numStudents = input("Enter the number of students that need to be recorded: ")

#program terminates if the user did not enter a digit
if numStudents.isdigit() == False:
    print("Invalid number of students entered.")

#otherwise valid input of student numbers
else:
    numStudents = int(numStudents) #converts string to int
    for i in range(numStudents): #runs the amount of students that need to be entered
        name = input(f"Enter Student {i+1}'s name: ")
        score = input(f"Enter Student {i+1}'s score: ")

        if score.isdigit(): #checks if a valid digit was entered
            score = int(score)
            listStudents.append((score,name)) #adds student to the list
            continue
        else: #if a digit wasn't entered
            print("Invalid score input! Student has not been recorded.")
            continue
    #sorts list according to score
    listStudents.sort(reverse=True)

    #output of highest and second highest scoring student
    print(f"Highest Scoring student:\t Name: {listStudents[0][1]}\tScore: {listStudents[0][0]}")
    print(f"Second Highest Scoring student:\t Name: {listStudents[1][1]}\tScore: {listStudents[1][0]}")




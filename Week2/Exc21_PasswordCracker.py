#variable initialization and user input
actualPassword = "MDX123"
guessPassword = input("Guess my password: ")

accuracy = 0 #starting accuracy

#loop runs for every character in the guessed password
for i in range(len(guessPassword)):
    if i < len(actualPassword): #compares length of input password with actual password
        if guessPassword[i] == actualPassword[i]: 
            accuracy += 1 #adds a point to accuracy if the two characters match
    elif accuracy > 0 and i >= len(actualPassword): #elif statement to penalize longer passwords
        accuracy -=1

score = int((accuracy / len(actualPassword)*100)) #gets percentage without decimal (formatting)

if score < 100:
    print(f"Password was guessed with {score}% accuracy.")
else:
    print("Password cracked!") 


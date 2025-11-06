import re

with open("Les_Brown.txt", "r") as f:
    try:
        #removing capital letters to prevent the same words being counted separately
        contents = f.read().lower()
        #excluding punctuation spotted in the original text file 
        contents = re.sub(r'[\!\.\"\,\:]', '', contents)
        words = contents.split()

        # initializing a dictionary to count frequency - matches key:value structure
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        #writing to a new file with the word and corresponding frequency
        with open("word_count.txt", "w") as f:
            try:
                for word in frequency:
                    f.write(f"{word}: {frequency[word]}\n")
                print("File successfully created.")
            except FileExistsError:
                print("File already exists.")
    except FileNotFoundError:
        print("Text file not found.")


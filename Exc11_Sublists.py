def isSublist(smaller, larger):
    '''
    Determines if a list is a sublist of another through input parameters of two lists
    Returns True or False
    '''
    #checks if the first list is smaller
    if len(smaller)>len(larger):
        return False

    else:
        if len(smaller) == 0: #if the list is empty its automatically a sublist
            return True
        for i in smaller: #loop runs through smaller sublist
            if i not in larger: #not a sublist condition
                return False
                break
        return True #default is return True

#initialization of the two lists and input boolean
stop = True
list1 = []
list2 = []

#start of user input for lists
print("Entering elements for lists. Type stop to end input.")

#while loop for user input of loop 1
while(stop):
    listElement = input("Enter element for list 1:\t")
    if listElement.lower() != "stop":
        list1.append(listElement)
    else:
        stop = False

#resetting stop boolean to create the second list
stop = True

#while loop for user input of loop 2
while(stop):
    listElement = input("Enter element for list 2:\t")
    if listElement.lower() != "stop":
        list2.append(listElement)
    else:
        stop = False

#calling the isSublist function and displaying the result
if (isSublist(list1,list2)==1):
    print(f"List 1 is a sublist of List 2.\n\tList 1: {list1}\n\tList 2: {list2}")
else:
    print(f"List 1 is a NOT sublist of List 2.\n\tList 1: {list1}\n\tList 2: {list2}")
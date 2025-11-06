from datetime import datetime

#user inputs for auth event
user = input("Enter username: ")
action = input("Enter desired action (LOGIN/LOGOFF): ")

if action.upper() != "LOGIN" and action.upper() != "LOGOFF": #user inputs in mixed cases will be accepted
    print("Entered action is invalid.") #for actions which are not login/logoff
else:
    #datetime formatted in %Y-%m-%d %H:%I:%M and format in given answer in question
    print(f"[{datetime.now().strftime("%Y-%m-%d %H:%I:%M")}] {action.upper()} user={user}")


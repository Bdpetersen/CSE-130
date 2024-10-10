# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program opens the json file then asks for the Username/Password. Then checks for the username and password in the same index
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to check for the username/password combo in the data. I evenually found out how to fix it and get it to work.
# 5. How long did it take for you to complete the assignment?
#      This took about 1 and a half hours.
import json

try:
    # Open and load the file into a dictionary.
    lab_data = open('Lab02.json', 'r')
    data = json.load(lab_data)
    lab_data.close()

# Error handling for opening the file.
except:
    print("Files not found, please fix.")

# Ask for the username/password
#user = input("Please Enter Your Username: ")
#password = input("Please Enter Your Password: ")

# Check if Username and Password matches
def authenticate(user, password):
    try:
        user_index = data['username'].index(user)
        match = password == data['password'][user_index]
    except:
        match = False

    if match == True:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

if __name__ == "__main__":
    authenticate("John Cheese", "None shall pass")
    authenticate("Black Knight", "Tis but a scratch.")
    authenticate("John Cheese", "Tis but a scratch.")
    authenticate("King Arthur", "Bring out your dead!")
    authenticate("Black Knight", "None shall pass")
    authenticate("King Arthur", "Run away!")
    authenticate("French Soldier", "I fart in your general direction")

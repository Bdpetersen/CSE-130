# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json
valid = False
with open("Lab02.json", "r") as lab_data:
    data = json.load(lab_data)

in_username = input("Please Enter Your Username: ")
in_password = input("Please Enter Your Password: ")

for item in range(len(data['username'])):
    if in_username == data['username'][item] and in_password == data['password'][item]:
        print("You are authenticated!")
        valid = True
if valid == False:
    print("You are not authorized to use the system.")
# 1. Name:
#       Brandon Petersen
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


all_prop = input("Do you own all the green properties? (y/n) ")
if all_prop == "y":
    # Find out what is on Pennsylvania
    pa_prop = int(input(
        "What is on Pennsylvania Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))
    # Find out if pennsylania needs a hotel
    if pa_prop <= 4:
        # Find out what is on North Carolina
        nc_prop = int(input(
            "What is on North Carolina Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))
        if nc_prop <= 4:
            # Find out what is on pacific
            pc_prop = int(input(
                "What is on Pacific Avenue? (0:nothing, 1:one house, 2:two houses, 3:three houses, 4:four houses, 5:a hotel) "))
            if pc_prop <= 4:
                hotels = input("How many hotels are there to purchase? ")
                if hotels > 0:
                    pa_needed = 4 - pa_prop
                    nc_needed = 4 - nc_prop
                    pc_needed = 4 - pc_prop
                    total_needed = pa_needed + nc_needed + pc_needed
                    cash_needed = total_needed * 200 + 200
                    cash = int(input("How much cash do you have to spend? "))
                    if cash >= cash_needed:
                        houses = int(
                            input("How many houses are there to purchase? "))
                        if houses >= total_needed:
                            print(
                                f"This will cost ${cash_needed}. \n Purchase 1 hotel and {total_needed} house(s). \n Put 1 hotel on Pennsylvania and return any houses to the bank.")
                            if nc_needed > 0:
                                print(
                                    f"Put {nc_needed} house(s) on North Carolina.")
                            if pc_needed > 0:
                                print(f"Put {pc_needed} house(s) on Pacific.")
                        else:
                            print(
                                "There are not enough houses available for purchase at this time.")

                    else:
                        print(
                            "You do not have sufficient funds to purchase a hotel at this time.")
                else:
                    print(
                        "There are not enough hotels available for purchase at this time.")
            else:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        else:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")

    else:
        print("You cannot purchase a hotel if the property already has one.")
else:
    print("You cannot purchase a hotel until you own all the properties of a given color group.")

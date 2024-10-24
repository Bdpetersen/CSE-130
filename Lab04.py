# 1. Name:
#       Brandon Petersen
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Find out the best way to put a hotel on pennsylvania avenue
# 4. What was the hardest part? Be as specific as possible.
# The hard part of the assignment I think was trying to figure out what the best way optimize the code is. I had a bunch of if statements in a chain so i had to decide if i needed all of them.
# 5. How long did it take for you to complete the assignment?
#      2 hours


def get_property_status(property_name, value):
    # return int(input(f"What is on {property_name}? (0: nothing, 1: one house, 2: two houses, 3: three houses, 4: four houses, 5: a hotel) "))
    return value


def can_purchase(cash, cash_needed, houses, total_needed):
    if cash < cash_needed:
        return "You do not have sufficient funds to purchase a hotel at this time."
    if houses < total_needed:
        return "There are not enough houses available for purchase at this time."
    return True


def purchase_hotel(cash_needed, total_needed, pa_needed, nc_needed, pc_needed):
    result = [f"This will cost ${cash_needed}. Purchase 1 hotel and {total_needed} house(s).",
              "Put 1 hotel on Pennsylvania and return any houses to the bank."]
    if nc_needed > 0:
        result.append(f"Put {nc_needed} house(s) on North Carolina.")
    if pc_needed > 0:
        result.append(f"Put {pc_needed} house(s) on Pacific.")
    return "\n".join(result)


def check_purchase(all_prop, pc_prop, nc_prop, pa_prop, houses, hotels, cash):
    # all_prop = input("Do you own all the green properties? (y/n) ")
    if all_prop == "y":
        # Find out what is on Pennsylvania
        # pa_prop = get_property_status("Pennsylvania Avenue")
        # Find out if pennsylania needs a hotel
        if pa_prop <= 4:
            # nc_prop = get_property_status("North Carolina Avenue")
            if nc_prop <= 4:
                # pc_prop = get_property_status("Pacfic Avenue")
                if pc_prop <= 4:
                    # hotels = int(input("How many hotels are there to purchase? "))
                    if hotels > 0:
                        pa_needed = 4 - pa_prop
                        nc_needed = 4 - nc_prop
                        pc_needed = 4 - pc_prop
                        total_needed = pa_needed + nc_needed + pc_needed
                        cash_needed = total_needed * 200 + 200
                        # cash = int(input("How much cash do you have to spend? "))
                        # houses = int(input("How many houses are there to purchase? "))
                        purchase_check = can_purchase(
                            cash, cash_needed, houses, total_needed)
                        if purchase_check == True:
                            return purchase_hotel(cash_needed, total_needed, pa_needed, nc_needed, pc_needed)
                        else:
                            return purchase_check
                    else:
                        return "There are not enough hotels available for purchase at this time."
                else:
                    return "Swap Pacific's hotel with Pennsylvania's 4 houses."
            else:
                return "Swap North Carolina's hotel with Pennsylvania's 4 houses."
        else:
            return "You cannot purchase a hotel if the property already has one."
    else:
        return "You cannot purchase a hotel until you own all the properties of a given color group."


def main():
    print(check_purchase("n", 0, 0, 0, 10, 10, 1000))
    print(check_purchase("y", 0, 0, 0, 15, 10, 100))
    print(check_purchase("y", 0, 0, 0, 10, 10, 9000))
    print(check_purchase("y", 5, 4, 4, 0, 0, 0))
    print(check_purchase("y", 4, 5, 4, 0, 0, 0))
    print(check_purchase("y", 4, 4, 5, 10, 10, 1000))
    print(check_purchase("y", 0, 0, 0, 12, 3, 3000))
    print(check_purchase("y", 3, 3, 3, 3, 1, 5000))


if __name__ == "__main__":
    main()

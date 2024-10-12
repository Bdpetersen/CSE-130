def get_property_status(property_name):
    return int(input(f"What is on {property_name}? (0: nothing, 1: one house, 2: two houses, 3: three houses, 4: four houses, 5: a hotel) "))


def can_purchase(cash, cash_needed, houses, total_needed):
    if cash < cash_needed:
        print("You do not have sufficient funds to purchase a hotel at this time.")
        return False
    if houses < total_needed:
        print("There are not enough houses available for purchase at this time.")
        return False
    return True


def purchase_hotel(cash_needed, total_needed, pa_needed, nc_needed, pc_needed):
    print(f"This will cost ${cash_needed}. \n Purchase 1 hotel and {total_needed} house(s). \n Put 1 hotel on Pennsylvania and return any houses to the bank.")
    if nc_needed > 0:
        print(f"Put {nc_needed} house(s) on North Carolina.")
    if pc_needed > 0:
        print(f"Put {pc_needed} house(s) on Pacific.")


def main():
    all_prop = input("Do you own all the green properties? (y/n) ")

    if all_prop == "y":
        pa_prop = get_property_status("Pennsylvania Avenue")

        if pa_prop <= 4:
            nc_prop = get_property_status("North Carolina Avenue")

            if nc_prop <= 4:
                pc_prop = get_property_status("Pacific Avenue")

                if pc_prop <= 4:
                    hotels = int(
                        input("How many hotels are there to purchase? "))

                    if hotels > 0:
                        pa_needed = 4 - pa_prop
                        nc_needed = 4 - nc_prop
                        pc_needed = 4 - pc_prop
                        total_needed = pa_needed + nc_needed + pc_needed
                        cash_needed = total_needed * 200 + 200

                        cash = int(
                            input("How much cash do you have to spend? "))
                        houses = int(
                            input("How many houses are there to purchase? "))

                        if can_purchase(cash, cash_needed, houses, total_needed):
                            purchase_hotel(cash_needed, total_needed,
                                           pa_needed, nc_needed, pc_needed)

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


if __name__ == "__main__":
    main()

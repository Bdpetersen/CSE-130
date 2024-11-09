# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#       sort a list by going through the unsorted part and finding the biggest number and put it to the back
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out what asserts would be usefull/ helpful in my program. Another thing was figuring out how to show the list with each item on a new line.
# 5. How long did it take for you to complete the assignment?
#      this program took me about two hours to finish.

import json


def sort(file_name):
    try:
        lab_data = open(file_name, 'r')  # Open the file. O(1)
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)           # O(n)
        lab_data.close()  # Close file we dont need it open anymore. O(1)

        data_list = data["array"]  # Put the data in a list. O(1)
        assert isinstance(
            data_list, list), "'array' should be a list in the file."
    except:
        return "File/Data not found."  # error handling if the file has an error

    print(f"\nThe values in {file_name} are: \n")

    # Checks if there is something to sort in the first place and returns nothing O(1)
    if not data_list:
        print("The list has no values")  # O(1)
        pass

    assert data_list is not None, "Data list should not be empty."

    initial_length = len(data_list)
    # For every item in the list O(n)
    for index in range(len(data_list)):
        max_index = 0  # Make max_index avaiable outside of the loop

        # for every item in the unsorted part of the list Find the maximum element in the unsorted part of the list O(n)
        for index2 in range(len(data_list) - index):
            if data_list[index2] > data_list[max_index]:
                max_index = index2
        # swaps the position of the items in the list.
        swap_position = len(data_list) - index - 1
        temp = data_list[max_index]
        data_list[max_index] = data_list[swap_position]
        data_list[swap_position] = temp

        assert data_list[swap_position] == temp, "Swap did not place the maximum value correctly."

    assert len(
        data_list) == initial_length, "The length of the list is not the same."
    return data_list


def main():
    version = input("Would you like to run the test cases? ")
    if version == 'y':
        print(f"{'\n'.join(sort("Lab08.empty.json"))}")
        print(f"{'\n'.join(sort("Lab08.trivial.json"))}")
        print(f"{'\n'.join(sort("Lab08.languages.json"))}")
        print(f"{'\n'.join(sort("Lab08.states.json"))}")
        print(f"{'\n'.join(sort("Lab08.cities.json"))}")

    else:
        file_name = input("What file would you like to open? ")
        print(f"{'\n'.join(sort(file_name))}")


if __name__ == '__main__':
    main()

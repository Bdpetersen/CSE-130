import json


def sort(file_name):
    try:
        lab_data = open(file_name, 'r')  # Open the file. O(1)
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)           # O(n)
        lab_data.close()  # Close file we dont need it open anymore. O(1)

        data_list = data["array"]  # Put the data in a list. O(1)
    except:
        return "File/Data not found."

    print(f"\nThe values in {file_name} are: \n")

    if not data_list:
        print("The list is empty")
        pass
    for index in range(len(data_list)):
        max_index = 0  # Initialize max_index

        # Find the maximum element in the unsorted part of the list
        for index2 in range(len(data_list) - index):
            if data_list[index2] > data_list[max_index]:
                max_index = index2

        swap_position = len(data_list) - index - 1
        temp = data_list[max_index]
        data_list[max_index] = data_list[swap_position]
        data_list[swap_position] = temp

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

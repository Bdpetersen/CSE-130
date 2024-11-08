def sort(file_name):
    try:
        lab_data = open(file_name, 'r')  # Open the file. O(1)
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)           # O(n)
        lab_data.close()  # Close file we dont need it open anymore. O(1)

        data_list = data["array"]  # Put the data in a list. O(1)
    except:
        return "File/Data not found."
    return "dsfg"


def main():
    version = input("Would you like to run the test cases? ")
    if version == 'y':
        print(sort("Lab08.empty.json"))
        print(sort("Lab08.trivial.json"))
        sort("Lab08.languages.json")
        sort("Lab08.states.json")
        sort("Lab08.cities.json")
    else:
        file_name = input("What file would you like to open? ")
        print(sort(file_name))


if __name__ == '__main__':
    main()

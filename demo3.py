import json
# Ask what file they want to search through.
# file_name = input("What is the name of the file?") #O(1)
try:
    lab_data = open("Lab08.languages.json", 'r')  # Open the file. O(1)
    # Loads the data of the file into a dictionary.
    data = json.load(lab_data)           # O(n)
    lab_data.close()  # Close file we dont need it open anymore. O(1)

    data_list = data["array"]  # Put the data in a list. O(1)
except:
    print("File/Data not found.")  # O(1)

if data_list:
    print("hello")

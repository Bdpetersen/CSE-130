# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Search a list by checking if the word your searching for matches the middle element, the search is complete. If the target is smaller than the middle element, then repeat with the lower numbers. if the target is larger, focus on the upper numbers.
# 4. Algorithmic Efficiency
#      O(n): The load method I used loops through one by one.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to get the data in the file into a list to use it in the comparisons. I knew how to have the data in a dictionary but i didnt know how to make it into a list.
# 6. How long did it take for you to complete the assignment?
#      This took about 2 hours to complete

import json


def main(file_name, target):
    # Ask what file they want to search through.
    # file_name = input("What is the name of the file?") #O(1)
    try:
        lab_data = open(file_name, 'r')  # Open the file. O(1)
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)           # O(n)
        lab_data.close()  # Close file we dont need it open anymore. O(1)

        data_list = data["array"]  # Put the data in a list. O(1)
    except:
        return "File/Data not found."  # O(1)
    # Ask for which name you are searching for
    # target = input("What name are we looking for?") #O(1)

    # set the varibles for the minimum and maximum.
    mini = 0  # O(1)
    maxi = len(data_list) - 1  # O(1)

    # Loops through all the list until minimum is less than or equal to maximum O(log n)
    while mini <= maxi:
        # Use integer division to find the middle O(1)
        mid = (mini + maxi) // 2

        # Checks if the list item is the target and returns if it is O(1)
        if data_list[mid] == target:
            # O(1)
            return f"We found {data_list[mid]} in {file_name} at index {mid}."
        # Checks if the list item is less than the target and if it is makes the minimum the middle number + 1 O(1)
        elif data_list[mid] < target:
            mini = mid + 1  # O(1)
        # The only other option would be to make the maximum highier. O(1)
        else:
            maxi = mid - 1  # O(1)
    # Returns not found if its not in the list
    return f"{target} is not found in {file_name}."  # O(1)


# runs the function O(1)
if __name__ == "__main__":
    print(main("Lab06.empty.json", "Empty"))  # O(1)
    print(main("Lab06.trivial.json", "trivial"))  # O(1)
    print(main("Lab06.trivial.json", "missing"))  # O(1)
    print(main("Lab06.languages.json", "C++"))  # O(1)
    print(main("Lab06.languages.json:", "Lisp"))  # O(1)
    print(main("Lab06.countries.json", "United States of America"))  # O(1)
    print(main("Lab06.countries.json", "United States"))  # O(1)

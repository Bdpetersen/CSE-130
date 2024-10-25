import json


def main():
    # Ask what file they want to search through.
    file_name = input("What is the name of the file?")
    try:
        lab_data = open(file_name, 'r')  # Open the file.
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)
        lab_data.close()  # Close file we dont need it open anymore.

        data_list = data["array"]  # Put the data in a list.
    except:
        return "File/Data not found."
    # Ask for which name you are searching for
    target = input("What name are we looking for?")

    # set the varibles for the minimum and maximum.
    mini = 0
    maxi = len(data_list) - 1

    while mini <= maxi:  # Loops through all the list until minimum is less than or equal to maximum
        mid = (mini + maxi) // 2  # Use integer division to find the middle

        if data_list[mid] == target:  # Checks if the list item is the target and returns if it is
            return f"We found {data_list[mid]} in {file_name} at index {mid}."
        # Checks if the list item is less than the target and if it is makes the minimum the middle number + 1
        elif data_list[mid] < target:
            mini = mid + 1
        else:  # The only other option would be to make the maximum highier.
            maxi = mid - 1
    # Returns not found if its not in the list
    return f"{target} is not found in {file_name}."


# runs the function
if __name__ == "__main__":
    main()

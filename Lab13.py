# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      go through a sub set of numbers and find the highest average in a list.
# 4. What was the hardest part? Be as specific as possible.
#      I had some trouble with getting the indexes correct in the for loop. i kept forgetting where to start and stop.
# 5. How long did it take for you to complete the assignment?
#      2 hours

import json


def compute_highest_average(file_name, window_size):
    try:
        lab_data = open(file_name, 'r')  # Open the file. O(1)
        # Loads the data of the file into a dictionary.
        data = json.load(lab_data)           # O(n)
        lab_data.close()  # Close file we dont need it open anymore. O(1)

        full_list = data["array"]  # Put the data in a list. O(1)
    except:
        return "Something is wrong with the file. Try Again!"

    assert isinstance(
        full_list, list), "Expected a list as input for full_list."
    assert isinstance(window_size, int), "Window size must be an integer."
    assert window_size > 0, "Window size must be greater than 0."
    assert len(
        full_list) >= window_size, "Window size cannot be larger than the list."
    current_sum = 0
    for i in range(0, window_size):
        current_sum += full_list[i]
    highest_avg = current_sum / window_size

    for i in range(window_size, len(full_list)):
        current_sum = current_sum - full_list[i - window_size] + full_list[i]
        current_avg = current_sum / window_size
        if current_avg > highest_avg:
            highest_avg = current_avg

    return highest_avg


def main():
    mode = input("Do you want to run an automated test? (y/n) ")

    if mode == "y":
        test_num = int(input("Which test would you like? "))
        if test_num == 1:
            print(compute_highest_average("130.13.small.json", 1000))
        else:
            print(compute_highest_average("banana.txt", 0))
            print(compute_highest_average("130.13.small.json", 10))
            print(compute_highest_average("130.13.large.json", 100))
    else:
        file_name = input("What file would you like to open?")
        window_size = input("What size would you like your subset to be?")
        print(compute_highest_average(file_name, int(window_size)))


if __name__ == "__main__":
    main()

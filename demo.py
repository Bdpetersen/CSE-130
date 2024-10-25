import json

# Load the data from the file
file_name = input("What is the name of the file? ")
with open(file_name, 'r') as lab_data:
    data = json.load(lab_data)

# Access the array of country names
countries = data["array"]
countries.sort()  # Ensure the list is sorted for binary search


def searching():
    target = input("What country are we looking for? ")

    mini = 0
    maxi = len(countries) - 1

    while mini <= maxi:
        mid = (mini + maxi) // 2  # Integer division for the mid-point
        guess = countries[mid]

        if guess == target:
            return f"Country '{target}' found at index {mid}."
        elif guess < target:
            mini = mid + 1
        else:
            maxi = mid - 1

    return f"Country '{target}' not found."


# Call the search function and print the result
print(searching())

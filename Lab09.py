# 1. Name:
#      Brandon Petersen
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      Find the days between two dates.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was finding how to do the asserts with my test cases. i had trouble with the asserts and then having them redo the input. Also had trouble with the check if end date is after start
# 5. How long did it take for you to complete the assignment?
#      This took me about two and a half hours to finish
def is_leap_year(year):
    ''' Return TRUE if a given year is a leap year '''
    assert year >= 1753

    # Years not divisible by 4 are guaranteed to not be a leap year.
    if year % 4 != 0:
        return False

    # Quad years not on the century are guaranteed to be a leap year.
    if year % 100 != 0:
        return True

    # Only quad-century years are leap years.
    return year % 400 == 0


def days_in_month(year, month):
    """Return the number of days in a specific month."""
    days_in_months = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29
    else:
        days_in_months[1] = 28

    return days_in_months[month - 1]


def days_between_dates(start_month, start_day, start_year, end_month, end_day, end_year):
    try:
        # Validate inputs are integers
        assert isinstance(start_month, int), "Start month must be an integer."
        assert isinstance(start_day, int), "Start day must be an integer."
        assert isinstance(start_year, int), "Start year must be an integer."
        assert isinstance(end_month, int), "End month must be an integer."
        assert isinstance(end_day, int), "End day must be an integer."
        assert isinstance(end_year, int), "End year must be an integer."

        # Validate the date
        assert start_year >= 1753 and end_year >= 1753, "Year cannot be less than 1753."
        assert 1 <= start_month <= 12 and 1 <= end_month <= 12, "Months must be between 1 and 12."
        assert 1 <= start_day <= days_in_month(
            start_year, start_month), "Invalid start day for given month/year."
        assert 1 <= end_day <= days_in_month(
            end_year, end_month), "Invalid end day for given month/year."
    except Exception as e:
        return f"Error: {e}. Please try again."

    if end_year < start_year or (end_year == start_year and end_month < start_month) or (end_year == start_year and end_month == start_month and end_day < start_day):
        return "Error: End date must be after the start date. Please try again."
    # Same month and year
    if start_year == end_year and start_month == end_month:
        return f"There are {end_day - start_day} day(s)."

    total_days = 0

    # Same year, different months
    if start_year == end_year:
        # Days remaining in start month
        total_days += days_in_month(start_year, start_month) - start_day

        # Days in full months between start and end
        for month in range(start_month + 1, end_month):
            total_days += days_in_month(start_year, month)

        # Days in end month
        total_days += end_day
        return f"There are {total_days} days."

    # years are different
    # Days remaining in start month
    total_days += days_in_month(start_year, start_month) - start_day

    # Days in remaining months of the start year
    for month in range(start_month + 1, 13):
        total_days += days_in_month(start_year, month)

    # Days in full years between start and end year
    for year in range(start_year + 1, end_year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365

    # Days in the odd months until end month
    for month in range(1, end_month):
        total_days += days_in_month(end_year, month)

    # Days in end month
    total_days += end_day

    return f"There are {total_days} days."


def main(mode):
    if mode == "y":
        print(days_between_dates(10, 4, 1752, 10, 4, 1855))
        print(days_between_dates(10, 3, 2005.3, 10, 2, 2007))
        print(days_between_dates(0, 3, 2005, 10, 2, 2007))
        print(days_between_dates(13, 3, 2005, 10, 2, 2007))
        print(days_between_dates(10, 0, 2005, 10, 2, 2007))
        print(days_between_dates(10, 40, 2005, 10, 2, 2007))
        print(days_between_dates(10, 3, 2005, 10, 2, 2002))
        print(days_between_dates(10, 4, 2005, 10, 4, 2005))
        print(days_between_dates(10, 4, 2005, 10, 24, 2005))
        print(days_between_dates(8, 4, 2005, 12, 4, 2005))
        print(days_between_dates(12, 25, 2005, 1, 8, 2006))
        print(days_between_dates(10, 4, 2003, 11, 23, 2024))

    else:
        start_year = int(input("Start Year: "))
        start_month = int(input("Start Month: "))
        start_day = int(input("Start Day: "))
        end_year = int(input("End Year: "))
        end_month = int(input("End Month: "))
        end_day = int(input("End Day: "))
        print(days_between_dates(start_month, start_day,
                                 start_year, end_month, end_day, end_year))


if __name__ == "__main__":
    mode = input("Would you like to run the Automated tests? (y/n) ")
    main(mode)

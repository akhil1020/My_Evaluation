# # 7. Date Difference Calculator (Real-World Scenario)
# Write a Python program that calculates the difference between two dates provided by a user.
# Scenario Example:
# A user wants to find out how many days they've lived by inputting their birthdate and today's date.
# Your program should:
# • Take two dates as input (format: dd-mm-yyyy).
# • Output the difference in days clearly.

#--------solution---------
from datetime import datetime

def date_difference(start_date_str, end_date_str):
    date_format = "%d-%m-%Y"
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)

    
    difference = end_date - start_date
    return difference.days

birthdate = input("Enter your birthdate (dd-mm-yyyy): ")
today = input("Enter today's date (dd-mm-yyyy): ")

days_lived = date_difference(birthdate, today)
print(f"\nit's  {days_lived} days.")

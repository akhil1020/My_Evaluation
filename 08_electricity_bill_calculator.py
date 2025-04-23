# 8. Electricity Bill Calculation (Business Logic)
# An electricity provider charges consumers based on slabs of electricity usage:
# Usage (kWh) Price per unit ( )₹
# 0-100 5
# 101-300 7
# 301-500 10
# Above 500 15
# Write a Python program that:
# • Accepts electricity usage (in kWh) from the user.
# • Clearly calculates and displays the bill, explaining the charges for each slab separately.
# Example Input: 450 kWh
# Example Output:
# Electricity Bill:
# 0-100 units @ 5/unit = 500₹ ₹
# 101-300 units @ 7/unit = 1400₹ ₹
# 301-450 units @ 10/unit = 1500₹ ₹
# Total Amount Payable = 3400

#-----solution---------
def calculate_electricity_bill(units):
    total_bill = 0
    print("\nElectricity Bill:")

    if units <= 100:
        charge = units * 5
        print(f"0-100 units @ 5/unit = ₹{charge}")
        total_bill += charge

    elif units <= 300:
        charge1 = 100 * 5
        charge2 = (units - 100) * 7
        print(f"0-100 units @ 5/unit = ₹{charge1}")
        print(f"101-{units} units @ 7/unit = ₹{charge2}")
        total_bill += (charge1 + charge2)

    elif units <= 500:
        charge1 = 100 * 5
        charge2 = 200 * 7
        charge3 = (units - 300) * 10
        print(f"0-100 units @ 5/unit = ₹{charge1}")
        print(f"101-300 units @ 7/unit = ₹{charge2}")
        print(f"301-{units} units @ 10/unit = ₹{charge3}")
        total_bill += (charge1 + charge2 + charge3)

    else:
        charge1 = 100 * 5
        charge2 = 200 * 7
        charge3 = 200 * 10
        charge4 = (units - 500) * 15
        print(f"0-100 units @ 5/unit = ₹{charge1}")
        print(f"101-300 units @ 7/unit = ₹{charge2}")
        print(f"301-500 units @ 10/unit = ₹{charge3}")
        print(f"501-{units} units @ 15/unit = ₹{charge4}")
        total_bill += (charge1 + charge2 + charge3 + charge4)

    print(f"\nTotal Amount Payable = ₹{total_bill}")

# Input from user
usage = int(input("Enter electricity usage (in kWh): "))
calculate_electricity_bill(usage)

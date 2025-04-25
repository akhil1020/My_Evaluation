# 10. Solve in Fewest Steps
# Given a string consisting of letters and digits, write a Python program to separate and sort letters
# and digits individually and then concatenate them, letters first and digits after, with each group
# sorted individually.
# Your solution should be concise yet clear.
# Example:
# • Input: "B4A1D3"
# • Output: "ABD134"

#
#-----solution---------
def solve_in_fewest_steps(s):
    letters = ''.join(sorted([ch for ch in s if ch.isalpha()]))
    digits = ''.join(sorted([ch for ch in s if ch.isdigit()]))
    
    return letters + digits


input_string = "B4A1D3"
output_string = solve_in_fewest_steps(input_string)
print(output_string)

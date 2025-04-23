# 1. Seating Arrangement Problem
# You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd
# like to sit next to. Write a Python function that:
# • Accepts the number of guests and their neighbor preferences.
# • Determines a valid circular seating arrangement satisfying all preferences.
# • If no arrangement is possible, clearly state that.
# Input Example:
# guests = {
# 'Alice': ['Bob', 'Carol'],
# 'Bob': ['Alice', 'David'],
# 'Carol': ['Alice', 'David'],
# 'David': ['Bob', 'Carol']
# }
# Output Example:
# ['Alice', 'Bob', 'David', 'Carol']

#---------solution--------->

from itertools import permutations

def is_valid_arrangement(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left = arrangement[(i - 1) % n]
        right = arrangement[(i + 1) % n]
        if not (left in preferences[guest] and right in preferences[guest]):
            return False
    return True

def find_seating_arrangement(guests):
    names = list(guests.keys())
    for perm in permutations(names):
        if is_valid_arrangement(perm, guests):
            return list(perm)
    return "No valid seating arrangement possible."


guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

# Output
print(find_seating_arrangement(guests))


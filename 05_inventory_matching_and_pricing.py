# 5. Inventory Matching and Pricing
# You have an inventory of products, each with a specific quantity and unit price. Customers place
# orders with a budget. Write a Python program to:
# • Determine if an order can be completely fulfilled within a customer's budget.
# • Prioritize items based on available quantities and prices.
# • Clearly state if the order is fulfillable, partially fulfillable, or impossible.

#---------solution---------

def check_order(inventory, order, budget):
    total_cost = 0
    fulfilled_order = {}
    partial = False

    for item, qty_requested in order.items():
        if item not in inventory:
            print(f"{item} is not available in inventory.")
            continue

        available_qty = inventory[item]['quantity']
        unit_price = inventory[item]['price']

        if available_qty >= qty_requested:
            cost = qty_requested * unit_price
            if total_cost + cost <= budget:
                total_cost += cost
                fulfilled_order[item] = qty_requested
            else:
                partial = True
                break
        else:
            partial = True
            cost = available_qty * unit_price
            if total_cost + cost <= budget:
                total_cost += cost
                fulfilled_order[item] = available_qty
            else:
                break

    print("\n--- Order Summary ---")
    if not fulfilled_order:
        print("Order is impossible to fulfill within the budget.")
    elif fulfilled_order == order:
        print("Order can be fully fulfilled.")
        print(f"Total Cost: {total_cost}")
    else:
        print("Order is partially fulfillable.")
        print(f"Fulfilled items: {fulfilled_order}")
        print(f"Total Cost: {total_cost}")



inventory = {
    'apple': {'quantity': 100, 'price': 2},
    'banana': {'quantity': 50, 'price': 1},
    'orange': {'quantity': 30, 'price': 3}
}

order = {
    'apple': 10,
    'banana': 20,
    'orange': 15
}

budget = 80


check_order(inventory, order, budget)

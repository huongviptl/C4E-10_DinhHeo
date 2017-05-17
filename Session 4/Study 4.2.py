def add_fruit(inven, fruit, quantity = 0):
    inven[fruit] = inven.get(fruit, 0) + quantity
    return

new_inven = {}

add_fruit(new_inven, "strawberries", 10)
print("strawberries: ",new_inven["strawberries"])

add_fruit(new_inven, "strawberries", 25)
print("strawberries: ",new_inven["strawberries"])
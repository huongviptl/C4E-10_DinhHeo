clothes = ["T-Shirt", "Sweater", "Jeans"]

print ("*******************************************")
print ("Add = A, Refesh = R, Update = U, Delete = D")
print ("*******************************************")

while True:

    print()
    action = input("Welcome to our shop, what do you want (A, R, U, D) ?")
    print(action)
    action = action.upper()
   
    
    print("Items in shop: ")
    item_no = 1
    for clothe in clothes:
        print("{0}.{1}".format(item_no, clothe))
        item_no += 1

    if action == "A":
        item = input("Add new item: ")
        clothes.append(item)

    elif action == "R":
        print()
        print("Refresh item !!")
        
    elif action == "U":
        item_no = int(input("Update new index: "))-1
        item_new = input("New item: ")
        clothes.insert(item_no, item_new)

    elif action == "D":
        item_del = input("Delete item: ")
        clothes.remove(item_del)

    

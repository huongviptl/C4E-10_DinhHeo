def extract_even(list_1):
    return [i for i in list_1 if i % 2 == 0]

print( "New List: ", extract_even([1, 4, 5, -1, 10]))

even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
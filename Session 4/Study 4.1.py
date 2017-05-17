text = input("Write something, please: ")
letter_counts = {}

for letter in text:
    letter_counts[letter] = letter_counts.get(letter, 0) +1

letter_items = list (letter_counts.items())
letter_items.sort()

print(letter_items)
def remove_dollar_sign(s):
    return s.replace("$", "")


s = input("Enter a string with $: ")
print(remove_dollar_sign(s))
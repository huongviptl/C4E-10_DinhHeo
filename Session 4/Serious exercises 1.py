inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
    'pocket' : ['seashell','strange berry','lint']
}
inventory['backpack'].sort()
print("Backpack after sort: ", inventory['backpack'])

inventory['backpack'].remove('dagger')
print("Backpack after remove: ", inventory['backpack'])

inventory['gold'] += 50
print ("Gold: ", inventory['gold'])
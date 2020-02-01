def change(name):
    return name[0].upper() + name[1:].lower()


list1 = ['adam', 'LISA', 'barT']
list2 = list(map(change, list1))
print(list2)

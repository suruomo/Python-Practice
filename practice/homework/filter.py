f1 = [{'name': 'IBM', 'price': 36.6},
      {'name': 'Lenovo', 'price': 23.2},
      {'name': 'oldboy', 'price': 21.2},
      {'name': 'ocean', 'price': 10.2},
      ]

print(list(filter(lambda p: p['price'] >= 20, f1)))

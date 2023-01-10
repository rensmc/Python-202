# Maps using dictionaries

items = [
    {
        'product': 'shirt',
        'price': 100
    },
    {
        'product': 'pants',
        'price': 300
    },
    {
        'product': 'trousers',
        'price': 900
    },
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# Adding taxes

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items)) # Creating a new list with taxes
print(new_items)
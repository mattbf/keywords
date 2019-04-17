from pprint import pprint

# Define words list, product list, and empty keyword list
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
keywords_list = []

# loop through lists to append words and products together

for product in products:
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
pprint(keywords_list)

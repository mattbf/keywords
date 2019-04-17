from pprint import pprint
import pandas as pd

# Define words list, product list, and empty keyword list
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
keywords_list = []

# loop through lists to append words and products together

for product in products:
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
# Make the list a DataFrame and rename columns
keywords_df = pd.DataFrame.from_records(keywords_list, columns=['Ad Group', 'Keyword'])


pprint(keywords_df)

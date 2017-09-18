import os
import pyopenstates

apikey = os.environ.get('API_KEY')

print(apikey)

pyopenstates.set_api_key(apikey)

# specify state in one place
state = 'ny'

# uses specific argument in function
metadata = pyopenstates.get_metadata(state)

# refer to metadata documentation
# https://openstates.github.io/pyopenstates/data%20structures.html#metadata
print(metadata.get('name'))
print(metadata.get('abbreviation'))
print(metadata.get('capitol_timezone'))

# https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
# uses keyworded argument in function
search_terms = 'guns'
bills = pyopenstates.search_bills(state=state, q=search_terms)

# print the output of the search_bills
# this is a list with items in the format of https://openstates.github.io/pyopenstates/data%20structures.html#bill
# print(bills)

# loop through list and output the name
for bill in bills:
    print(bill.get('bill_id'))
    print(bill.get('title'))
    print('---------------------------------------------------')
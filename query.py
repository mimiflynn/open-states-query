import os
import pyopenstates

apikey = os.environ.get('OPENSTATES_API_KEY')

# specify state in one place
state = 'ny'

# file name to output
file = 'openstates.txt'

# output above configuration
print('apikey ----------')
print(apikey)
print('state -----------')
print(state)
print('file output -----')
print(file)

output = open(file, 'w')

pyopenstates.set_api_key(apikey)

# uses specific argument in function
metadata = pyopenstates.get_metadata(state)

# refer to metadata documentation
# https://openstates.github.io/pyopenstates/data%20structures.html#metadata
output.write(metadata.get('name') + '\n')
output.write(metadata.get('abbreviation') + '\n')
output.write(metadata.get('capitol_timezone') + '\n')
output.write('---------------------------------------------------\n')

# https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
# uses keyworded argument in function
search_terms = 'guns'
bills = pyopenstates.search_bills(state=state, q=search_terms)

# print the output of the search_bills
# this is a list with items in the format of https://openstates.github.io/pyopenstates/data%20structures.html#bill
# print(bills)

# loop through list and output the name
for bill in bills:
    output.write(bill.get('bill_id') + '\n')
    output.write(bill.get('title') + '\n')
    output.write('---------------------------------------------------\n')

output.close()

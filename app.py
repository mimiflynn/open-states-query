from datetime import datetime
import os
import pyopenstates
import sys

import formatcsv
import query

apikey = os.environ.get('OPENSTATES_API_KEY')
search = sys.argv[1]
directory_name = sys.argv[2]

# create directory to house data per search term
dir_name = directory_name + '/' + search
os.makedirs(dir_name)

# create README file for directory
info = '''
Contents of this directory were queried from openstates.org
Collected on {:%Y-%m-%d_%H-%M-%S}'''.format(datetime.now())

output = open(dir_name + '/' + 'README.md', 'wb')
output.write(formatcsv.encode_for_file(info))
output.close()


print('pyopenstates query')
print('-------------------------------------')
print('API Key - ' + apikey)
print('Search term - ' + search)
print('Output directory - ' + directory_name)


pyopenstates.set_api_key(apikey)


# query metadata
print('Querying metadata')
metadata = pyopenstates.get_metadata()


# create list of states from returned data
print('Process metadata')
states = list(map(query.get_state_abbr, metadata))


# loop through list of states and query for keywords
for state in states:
    bills = query.query_state(state, search)

    # output as CSV
    contents = formatcsv.prep_bill_for_csv(bills)
    file = dir_name + '/' + state + '-' + search + '-data.csv'
    formatcsv.csv_writer(file, contents)


# create dict with state key and number of bills
bill_count_by_state = {}

for state in states:
    bill_count_by_state[state] = len(us_bills[state])

print('Number of bills by state')
print(bill_count_by_state)


# create list of number of bills and add them together
values = bill_count_by_state.values()
values.sort()

print(values)

total_bills = 0

for value in values:
    total_bills = total_bills + value
    
print('Total number of bills in US')
print(total_bills)

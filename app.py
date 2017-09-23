import os
import pyopenstates
import sys

apikey = os.environ.get('OPENSTATES_API_KEY')

# search = sys.argv[1]
search = 'firearms'

def outputAbbr(state):
    print(state)
    return state.get('abbreviation')

def queryState(state, search_terms, directory):
    file = directory + '/' + state + '-' + search_terms + '-data.txt'

    output = open(file, 'w')

    metadata = pyopenstates.get_metadata(state)

    # refer to metadata documentation
    # https://openstates.github.io/pyopenstates/data%20structures.html#metadata
    output.write(metadata.get('name') + '\n')
    output.write(metadata.get('abbreviation') + '\n')
    output.write(metadata.get('capitol_timezone') + '\n')
    output.write('---------------------------------------------------\n')

    # https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
    # uses keyworded argument in function
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


pyopenstates.set_api_key(apikey)

# create directory to house data per search term
dir_name = 'data/' + search
os.makedirs(dir_name)

# query metadata
metadata = pyopenstates.get_metadata()
print(metadata)

# create list of states from returned data
states = list(map(outputAbbr, metadata))
print(states)

# loop through list of states and query for keywords
for state in states:
    queryState(state, search, dir_name)

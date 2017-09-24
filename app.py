import os
import pyopenstates
import sys

apikey = os.environ.get('OPENSTATES_API_KEY')
search = sys.argv[1]
dir = sys.argv[2]

print('pyopenstates query')
print('-------------------------------------')
print('API Key - ' + apikey)
print('Search terms - ' + search)
print('Output directory - ' + dir)

def encodeForFile(string):
    return ' '.join((string, '\n')).encode('utf-8').strip()

def getStateAbbr(state):
    return state.get('abbreviation')

def queryState(state, search_terms, directory):
    file = directory + '/' + state + '-' + search_terms + '-data.txt'

    output = open(file, 'wb')

    print('Query for ' + state + ' metadata')
    metadata = pyopenstates.get_metadata(state)

    # refer to metadata documentation
    # https://openstates.github.io/pyopenstates/data%20structures.html#metadata
    output.write(encodeForFile(metadata.get('name')))
    output.write(encodeForFile(metadata.get('abbreviation')))
    output.write(encodeForFile(metadata.get('capitol_timezone')))
    output.write(encodeForFile('---------------------------------------------------'))

    # https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
    # uses keyworded argument in function
    print('Query for ' + state + ' bills')
    bills = pyopenstates.search_bills(state=state, q=search_terms)

    # print the output of the search_bills
    # this is a list with items in the format of https://openstates.github.io/pyopenstates/data%20structures.html#bill
    # print(bills)

    # loop through list and output the name
    for bill in bills:
        output.write(encodeForFile(bill.get('bill_id')))
        output.write(encodeForFile(bill.get('title')))
        output.write(encodeForFile('---------------------------------------------------'))

    output.close()


pyopenstates.set_api_key(apikey)

# create directory to house data per search term
dir_name = dir + '/' + search
os.makedirs(dir_name)

# query metadata
print('Querying metadata')
metadata = pyopenstates.get_metadata()

# create list of states from returned data
print('Process metadata')
states = list(map(getStateAbbr, metadata))

# loop through list of states and query for keywords
for state in states:
    queryState(state, search, dir_name)

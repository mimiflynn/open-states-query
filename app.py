import os
import pyopenstates
import sys

import query

apikey = os.environ.get('OPENSTATES_API_KEY')
search = sys.argv[1]
directory_name = sys.argv[2]

# create directory to house data per search term
dir_name = directory_name + '/' + search
os.makedirs(dir_name)


print('pyopenstates query')
print('-------------------------------------')
print('API Key - ' + apikey)
print('Search terms - ' + search)
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
    query.query_state(state, search, dir_name)

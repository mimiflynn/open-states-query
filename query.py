import pyopenstates

def encode_for_file(string):
    return ' '.join((string, '\n')).encode('utf-8').strip()


def get_state_abbr(state):
    return state.get('abbreviation')


def query_state(state, search_terms, directory):
    file = directory + '/' + state + '-' + search_terms + '-data.txt'

    output = open(file, 'wb')

    print('Query for ' + state + ' metadata')
    metadata = pyopenstates.get_metadata(state)

    # refer to metadata documentation
    # https://openstates.github.io/pyopenstates/data%20structures.html#metadata
    output.write(encode_for_file(metadata.get('name')))
    output.write(encode_for_file(metadata.get('abbreviation')))
    output.write(encode_for_file(metadata.get('capitol_timezone')))
    output.write(encode_for_file('---------------------------------------------------'))

    # https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
    # uses keyworded argument in function
    print('Query for ' + state + ' bills')
    bills = pyopenstates.search_bills(state=state, q=search_terms)

    # print the output of the search_bills
    # this is a list with items in the format of https://openstates.github.io/pyopenstates/data%20structures.html#bill
    # print(bills)

    # loop through list and output the name
    for bill in bills:
        output.write(encode_for_file(bill.get('bill_id')))
        output.write(encode_for_file(bill.get('title')))
        output.write(encode_for_file('---------------------------------------------------'))

    output.close()

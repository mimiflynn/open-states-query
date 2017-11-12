import pyopenstates


def get_state_abbr(state):
    return state.get('abbreviation')


def query_state(state, search_terms):
    """
    https://openstates.github.io/pyopenstates/pyopenstates%20module.html#pyopenstates.search_bills
    uses keyworded argument in function
    """
    print('Query for ' + state + ' bills')

    bills = pyopenstates.search_bills(state=state, q=search_terms)

    return bills

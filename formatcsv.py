import csv


def csv_writer(path, data):
    """
    Write data to a CSV file path
    https://www.blog.pythonlibrary.org/2014/02/26/python-101-reading-and-writing-csv-files/
    """
    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def encode_for_file(string):
    return string.encode('utf-8').strip()


def prep_bill_for_csv(bills):
    contents = [['bill_id', 'title']]

    # loop through list and output the name
    for bill in bills:
        contents.append([bill.get('bill_id'), bill.get('title')])

    return contents

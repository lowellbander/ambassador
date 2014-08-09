import csv
from collections import defaultdict

def main():
    print "Hello, world!"
    with open ('tour.csv', 'r') as handle:
        doc = csv.DictReader(handle, ['blank', 'date', 'name', 'time',
                                        'email', 'phone', 'comment', 'major'])
        for family in doc:
            if family['date'] == '11':
                print family



if __name__ == '__main__':
    main()

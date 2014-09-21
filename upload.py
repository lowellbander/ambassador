from pprint import pprint
import csv
import json
import settings
import sys
import unirest
from api import post

HEADERS = {'Accept':'application/json', 'Content-Type': 'application-json'}

def usage():
    print "Usage: %s <tour.csv>" % sys.argv[0]

def main():

    if len(sys.argv) is not 2:
        usage()
        return

    document = sys.argv[1]

    with open(document, 'r') as handle:
        doc = csv.DictReader(handle, ['blank', 'date', 'name', 'time',
                                    'email', 'phone', 'comment', 'major', 'nPeople'])

        remaining = 4
        for family in doc:

            #skip the first 4 lines
            if remaining is not 0:
                remaining -= 1
                continue

            tour = {'date': family['date'] + " " + family['time'],
                    'name': family['name'],
                    'email': family['email'],
                    'phone': family['phone'],
                    'comments': family['comment'],
                    'majors_of_interest': family['major'],
                    'nVisitors': family['nPeople']}
            pprint(post(tour))

if __name__ == "__main__":
    main()

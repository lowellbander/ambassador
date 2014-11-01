from pprint import pprint
import csv
import sys
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
        headers = ['blank', 'date', 'name', 'time', 'email', 'phone']
        headers.extend(['comment', 'major', 'nPeople'])
        doc = csv.DictReader(handle, headers)
        remaining = 4
        for family in doc:

            #skip the first 4 lines
            if remaining is not 0:
                remaining -= 1
                continue

            #skip empty rows
            if family['date'] == '':
                continue

            tour = {}
            tour['date'] = 'November ' + family['date'] + " " + family['time']
            tour['name'] = family['name']
            tour['email'] = family['email']
            tour['phone'] = family['phone']
            tour['comments'] = family['comment']
            tour['majorsOfInterest'] = family['major']
            tour['nVisitors'] = family['nPeople']
            pprint(post(tour))

if __name__ == "__main__":
    main()

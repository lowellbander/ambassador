
from pprint import pprint
import csv
import json
import settings
import sys
import unirest

HEADERS = {'Accept':'application/json', 'Content-Type': 'application-json'}

def usage():
    print "Usage: %s <tour.csv>" % sys.argv[0]

def get_all():
    response = unirest.get(settings.API_URL + 'tour/')
    return response.body

def post(tour):
    response = unirest.post(settings.API_URL + 'tour/', headers = HEADERS,
                                                params = json.dumps(tour))
    return response.body


def main():

    if len(sys.argv) is not 2:
        usage()
        return

    document = sys.argv[1]

    with open(document, 'r') as handle:
        doc = csv.DictReader(handle, ['blank', 'date', 'name', 'time',
                                    'email', 'phone', 'comment', 'major', 'nPeople'])
        for family in doc:
            print family
            tour = {'date': family['date'] + " " + family['time'],
                    'name': family['name'],
                    'email': family['email'],
                    'phone': family['phone'],
                    'comment': family['comment'],
                    'major_of_interest': family['major'],
                    'nVisitors': family['nPeople']}
            pprint(post(tour))

if __name__ == "__main__":
    main()

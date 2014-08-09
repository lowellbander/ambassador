import csv
from collections import defaultdict

def main():
    with open ('tour.csv', 'r') as handle:
        doc = csv.DictReader(handle, ['blank', 'date', 'name', 'time',
                                        'email', 'phone', 'comment', 'major', 'nPeople'])
        for family in doc:
            if family['date'] == '11':
                #print family
                print "Name: %s" % family['name']
                print "Email: %s" % family['email']
                print "Phone Number: %s" % family['phone']
                if family['comment'] != '':
                    print "Comments: %s" % family['comment']
                print "Major of Interest: %s" % family['major']
                print "Number of People: %s" % family['nPeople']
                print ""



if __name__ == '__main__':
    main()

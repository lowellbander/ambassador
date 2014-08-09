import csv
from collections import defaultdict

class Ambassador:
    name = ""
    email = ""
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        print "%s can be contacted using %s" % (self.name, self.email)

def print_tours():
    with open ('tour.csv', 'r') as handle:
        doc = csv.DictReader(handle, ['blank', 'date', 'name', 'time',
                                        'email', 'phone', 'comment', 'major', 'nPeople'])

        crossed_timeline = False
        print "~~~~ 10:00am ~~~~"
        print ""
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
                if not crossed_timeline and family['time'] == '1 PM':
                    crossed_timeline = True
                    print ""
                    print "~~~~ 1:00pm ~~~~"
                print ""

def init_amb():
    ambassadors = []
    with open('amb.csv','r') as handle:
        doc = csv.DictReader(handle, ['first', 'last', 'email'])
        for amb in doc:
            name = amb['first'] + ' ' + amb['last']
            print name
            ambassadors.append(Ambassador(name, amb['email']))
    return ambassadors


    #config = {'mon': {},
    #          'weds': {},
    #          'fri': {}}

def main():
    print_tours()
    #ambassadors = init_amb()
    #for amb in ambassadors:
    #print amb


if __name__ == '__main__':
    main()

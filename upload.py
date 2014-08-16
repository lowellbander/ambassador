from pprint import pprint
import json
import settings
import unirest

HEADERS = {'Accept':'application/json', 'Content-Type': 'application-json'}

def get_all():
    response = unirest.get(settings.API_URL + 'tour/')
    return response.body

def post(tour):
    response = unirest.post(settings.API_URL + 'tour/', headers = HEADERS,
                                                params = json.dumps(tour))
    return response.body

def main():
    #print "hello world"
    #pprint(get_all())
    tour = {'name': 'second'}
    pprint(post(tour))

if __name__ == "__main__":
    main()

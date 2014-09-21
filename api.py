import json
import unirest
import settings

HEADERS = {'Accept':'application/json', 'Content-Type': 'application-json'}

def get_all():
    response = unirest.get(settings.API_URL + 'tour/')
    return response.body['data']

def post(tour):
    response = unirest.post(settings.API_URL + 'tour/', headers = HEADERS,
                                                params = json.dumps(tour))
    return response.body


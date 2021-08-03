import requests
import json


def get_ids(url):
    listings_json = get_json_listings(url)
    json_str = (listings_json.json.return_value)

    return get_ids_from_json((json_str))

def get_json_listings(url):
    response = requests.get(url)
    if response.ok:
        return response
    else:
        return None

def get_ids_from_json(json):
    print(type(json))
    ids = []
    for listing in json:
        ids.append(listing['id'])
    return ids



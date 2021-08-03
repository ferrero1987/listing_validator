import requests
import json


def get_ids(url):
    listings_json = get_json_listings(url)
    return get_ids_from_json(listings_json.json.return_value)

def get_json_listings(url):
    response = requests.get(url)
    if response.ok:
        return response
    else:
        return None

def get_ids_from_json(json):
    ids = []
    for listing in json:
        ids.append(listing['id'])
    return ids

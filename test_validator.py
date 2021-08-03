from validator import get_ids
import unittest
import json
from unittest.mock import patch, Mock
from validator import get_json_listings, get_ids_from_json

class BasicTests(unittest.TestCase):

    def test_get_ids(self):
        mock_get_patcher = patch('validator.requests.get')
        with open('listing_validator\json_listings.txt', 'r') as file:
            listings = json.loads(file.read())

        mock_get = mock_get_patcher.start()

        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = listings

        ids = get_ids("http://jsonplaceholder.listingtest.com/listings")

        mock_get_patcher.stop()

        self.assertEqual(ids, ["01FA61T8NJXR9SFEW53FBS7XK2", "22FA61T8NJXR9SFEW53FBS7XK2"])

    def test_get_ids_from_json(self):

        with open('listing_validator\json_listings.txt', 'r') as file:
            listings = json.loads(file.read())

        self.assertEqual(get_ids_from_json(listings), ["01FA61T8NJXR9SFEW53FBS7XK2", "22FA61T8NJXR9SFEW53FBS7XK2"])
    
    def test_get_json_listings(self):

        mock_get_patcher = patch('validator.requests.get')
        with open('listing_validator\json_listings.txt', 'r') as file:
            listings = json.loads(file.read())
        

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of listings.
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = listings

        # Call the service, which will send a request to the server.
        response = get_json_listings("http://jsonplaceholder.listingtest.com/listings")

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], "01FA61T8NJXR9SFEW53FBS7XK2")
        self.assertEqual(response.json()[1]['id'], "22FA61T8NJXR9SFEW53FBS7XK2")

if __name__ == "__main__":
    unittest.main()

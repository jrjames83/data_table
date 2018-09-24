import unittest
import random

from data_loader import load_coin_data, grouped_data_loader
from flask_app import app



class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data = load_coin_data()
        self.grouped = grouped_data_loader('Name')

    def test_data_is_a_list(self):
        self.assertEqual(type(self.data), list)

    def test_length_of_data_list_is_gt10(self):
        self.assertGreater(len(self.data), 499)      

    def test_data_contains_dicts(self):
        self.assertEqual(type(random.choice(self.data)), dict)

    def test_grouped_data_loader_returns_dict(self):
        self.assertEqual(type(self.grouped), dict)


class TestVariousResponses(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)

    def test_api_response_without_parameters(self):
        response = self.app.get('/api/coins/')
        self.assertEqual(response.status_code,200)    

    def test_api_response_with_valid_name_filter(self):
        response = self.app.get('/api/coins/?name=bitcoin')
        self.assertEqual(response.status_code,200) 

    def test_api_response_with_valid_price_filter(self):
        response = self.app.get('/api/coins/?min_price=8000')
        self.assertEqual(response.status_code,200) 

    def test_api_response_with_valid_price_filter_and_valid_name_filter(self):
        response = self.app.get('/api/coins/?min_price=2000&name=ether')
        self.assertEqual(response.status_code,200)

    def test_api_response_with_valid_price_filter_and_valid_name_filter(self):
        response = self.app.get('/api/coins/?min_price=2000&name=ether')
        self.assertEqual(response.status_code,200)

    def test_api_responds_with_json(self):
        response = self.app.get('/api/coins/?min_price=2000&name=ether')
        self.assertEqual(response.content_type, 'application/json')
          
    def test_grouped_api_response_with_json(self):
        response = self.app.get('/api/groups/')
        self.assertEqual(response.content_type, 'application/json')



if __name__ == "__main__":
    unittest.main()
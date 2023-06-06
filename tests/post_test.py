import requests
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://172.25.0.4"
        self.headers = {"Content-Type": "application/json"}
        
        
    #test POST requests
    def test_create_entity(self):
        payload = {
            "fname": "John",
            "lname": "Doe",
            "phone": "+1234567890",
            "bday": "1990-01-01"
        }
        response = requests.post(self.base_url, json=payload, headers=self.headers, verify=False)
        print(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json().get("id"))
        
    def test_get_request_400_with_missings(self):
        payload = {
            "fname": "John",
            "lname": "Doe",
            "phone": "+1234567890"
        }
        response = requests.post(self.base_url, json=payload, headers=self.headers, verify=False)
        print(response.content)
        self.assertEqual(response.status_code, 400)
    
    def test_get_request_400_with_invalid_number(self):
        payload = {
            "fname": "John",
            "lname": "Doe",
            "phone": "1234567890",
            "bday": "1990-01-01"
        }
        response = requests.post(self.base_url, json=payload, headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 400)

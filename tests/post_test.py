import requests
import unittest
import socket
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class TestAPI(unittest.TestCase):
    def setUp(self):
        ip = socket.gethostbyname(str(socket.gethostname()))
        ip = ip[:-1] + '4'
        self.base_url = f"https://{ip}"
        self.headers = {"Content-Type": "application/json"}
        
    def test_create_entity(self):
        payload = {
            "fname": "John",
            "lname": "Doe",
            "phone": "+1234567890",
            "bday": "1990-01-01"
        }
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(self.base_url, json=payload, headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 400)

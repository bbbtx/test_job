import requests
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://172.25.0.4"
        self.headers = {"Content-Type": "application/json"}

    def test_get_request(self):
        
        response = requests.get(f"{self.base_url}/", headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    def test_get_request_by_id(self):

        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":"1","fname":"Tom","lname":"Hanks","phone":"+1123456789","bday":"1956-07-09"}])

    def test_get_request_by_fname(self):
    
        response = requests.get(f"{self.base_url}/?first_name=Tom", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":"1","fname":"Tom","lname":"Hanks","phone":"+1123456789","bday":"1956-07-09"}])

    def test_get_request_by_lname(self):
        
        response = requests.get(f"{self.base_url}/?last_name=Hanks", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":"1","fname":"Tom","lname":"Hanks","phone":"+1123456789","bday":"1956-07-09"}])

    def test_get_request_by_phone(self):
    
        response = requests.get(f"{self.base_url}/?phone_number=+1123456789", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":"1","fname":"Tom","lname":"Hanks","phone":"+1123456789","bday":"1956-07-09"}])

    def test_get_request_by_phone(self):
    
        response = requests.get(f"{self.base_url}/?birth_date=1956-07-09", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id":"1","fname":"Tom","lname":"Hanks","phone":"+1123456789","bday":"1956-07-09"}])
    
    def test_get_error_request(self):
    
        response = requests.get(f"{self.base_url}/?id=0", headers=self.headers)
        self.assertEqual(response.status_code, 404)

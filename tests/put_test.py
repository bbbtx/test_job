import requests
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://172.25.0.4"
        self.headers = {"Content-Type": "application/json"}
        self.person = {"id": 1, "fname": "John", "lname": "Doe", "phone": "+1234567890", "bday": "1990-01-01"}

    def test_put_request(self):

        updated_person = {"id": 1, "fname": "Jane", "lname": "Doe", "phone": "+0987654321", "bday": "1990-01-01"}
        response = requests.put(f"{self.base_url}/", headers=self.headers, json=updated_person, verify=False)
        self.assertEqual(response.status_code, 202)

        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), updated_person)

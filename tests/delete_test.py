import requests
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://172.25.0.4"
        self.headers = {"Content-Type": "application/json"}

    def test_delete_request(self):
        response = requests.delete(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 202)
        #Check
        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 404)
        
    def test_delete_deleted_item(self):
        response = requests.delete(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 404)

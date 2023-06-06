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

    def test_delete_request(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.delete(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 202)

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 404)
        
    def test_delete_deleted_item(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.delete(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 404)
        

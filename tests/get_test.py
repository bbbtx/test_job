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

    def test_get_request(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(f"{self.base_url}/", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 200)
    
    def test_get_request_by_id(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers,verify=False)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"], [{"id":"1","fname":"Jane","lname":"Doe","phone":"+0987654321","bday":"1990-01-01"}])
    
    def test_get_error_request(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(f"{self.base_url}/?id=0", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 404)

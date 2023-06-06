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
        self.person = {"id": 1, "fname": "John", "lname": "Doe", "phone": "+1234567890", "bday": "1990-01-01"}

    def test_put_request(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        updated_person = {"id": 1, "fname": "Jane", "lname": "Doe", "phone": "+0987654321", "bday": "1990-01-01"}
        response = requests.put(f"{self.base_url}/", headers=self.headers, json=updated_person, verify=False)
        self.assertEqual(response.status_code, 202)

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(f"{self.base_url}/?id=1", headers=self.headers, verify=False)
        self.assertEqual(response.status_code, 200 )
        self.assertEqual(response.json(), updated_person)
    
    def test_put_request_error(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        updated_person = {"id": 1, "fname": "Jane", "lname": "Doe", "phone": "11110987654321", "bday": "19900111"}
        response = requests.put(f"{self.base_url}/", headers=self.headers, json=updated_person, verify=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status_code, 500)

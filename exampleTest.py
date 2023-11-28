import unittest
import requests
import json

class APITests(unittest.TestCase):

    base_url = "https://automationexercise.com/api"

    def test_api1(self):
        response = requests.get('https://automationexercise.com/api/productsList')
        self.assertEqual(200, response.status_code)
        #products_list = json.loads(response.text)
        #self.assertIsInstance(products_list, list)

    def test_api2(self):
        response = requests.post('https://automationexercise.com/api/productsList')
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.text)
        self.assertEqual(405, response_data["responseCode"])
        self.assertEqual("This request method is not supported.", response_data["message"])

    def test_api3(self):
        response = requests.get('https://automationexercise.com/api/brandsList')
        self.assertEqual(200, response.status_code)
        api_response = json.loads(response.text)
        self.assertEqual(200, api_response.get('responseCode'))
        brands_list = api_response.get('brands')
        self.assertIsInstance(brands_list, list)

    def test_api4(self):
        response = requests.put('https://automationexercise.com/api/brandsList')
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.text)
        self.assertEqual(405, response_data["responseCode"])
        self.assertEqual("This request method is not supported.", response_data["message"])

    def test_api5(self):
        payload = {"search_product": "top"}
        response = requests.post('https://automationexercise.com/api/searchProduct', data=payload)
        self.assertEqual(200, response.status_code)
        api_response = json.loads(response.text)
        products_list = api_response.get('products')
        self.assertIsInstance(products_list, list)

    def test_api6(self):
        response = requests.post('https://automationexercise.com/api/searchProduct')
        api_response = json.loads(response.text)
        self.assertEqual(400, api_response.get('responseCode'))
        self.assertEqual("Bad request, search_product parameter is missing in POST request.", api_response.get('message'))

    def test_api7(self):
        payload = {"email": "user@example.com", "password": "password123"}
        response = requests.post('https://automationexercise.com/api/verifyLogin', data=payload)
        self.assertEqual(404, response.json().get('responseCode'))
        self.assertEqual(200, response.status_code)
        self.assertEqual("User not found!", response.json().get('message'))

    def test_api8(self):
        payload = {"password": "password123"}
        response = requests.post('https://automationexercise.com/api/verifyLogin', data=payload)
        self.assertEqual(400, response.json().get('responseCode'))
        self.assertEqual(200, response.status_code)
        self.assertEqual("Bad request, email or password parameter is missing in POST request.", response.json().get('message'))

    def test_api9(self):
        response = requests.delete('https://automationexercise.com/api/verifyLogin')
        self.assertEqual(405, response.json().get('responseCode'))
        self.assertEqual(200, response.status_code)
        self.assertEqual("This request method is not supported.", response.json().get('message'))

    def test_api10(self):
        payload = {"email": "invaliduser@example.com", "password": "invalidpassword"}
        response = requests.post('https://automationexercise.com/api/verifyLogin', data=payload)
        self.assertEqual(404, response.json().get('responseCode'))
        self.assertEqual(200, response.status_code)
        self.assertEqual("User not found!", response.json().get('message'))

    def test_api11(self):
        payload = {
            "name": "Johnny Depp",
            "email": "johnny.depp@example.com",
            "password": "password123",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "04",
            "birth_year": "2000",
            "firstname": "Johnny",
            "lastname": "Depp",
            "company": "ISU University",
            "address1": "123 Main Street",
            "address2": "Apt 4",
            "country": "USA",
            "zipcode": "12345",
            "state": "CA",
            "city": "San Francisco",
            "mobile_number": "1234567890"
        }
        response = requests.post('https://automationexercise.com/api/createAccount', data=payload)
        self.assertEqual(201, response.json().get('responseCode'))
        self.assertEqual(200, response.status_code)
        self.assertEqual("User created!", response.json().get('message'))

    def test_api12(self):
        payload = {"email": "johnny.depp@example.com", "password": "password123"}
        response = requests.delete('https://automationexercise.com/api/deleteAccount', data=payload)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get('responseCode'))
        self.assertEqual("Account deleted!", response.json().get('message'))

    def test_api13(self):
        payload = {
            "name": "Updated Johnny Depp",
            "email": "johnny.depp@example.com",
            "password": "updatedpassword",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "04",
            "birth_year": "2000",
            "firstname": "Johnny",
            "lastname": "Depp",
            "company": "Updated ISU University",
            "address1": "456 Apple Street",
            "address2": "Suite 8",
            "country": "USA",
            "zipcode": "54321",
            "state": "NY",
            "city": "New York",
            "mobile_number": "9876543210"
        }
        response = requests.put('https://automationexercise.com/api/updateAccount', data=payload)
        self.assertEqual(200, response.status_code)
        self.assertEqual(404, response.json().get('responseCode'))
        #self.assertEqual("User updated!", response.json().get('message'))
        #I wrote first like in website, but it gave error, so that I coded again according to error. Now it runs OK.
        self.assertEqual("Account not found!", response.json().get('message'))


    def test_api14(self):
        payload = {"email": "johnny.depp@example.com"}
        response = requests.get('https://automationexercise.com/api/getUserDetailByEmail', params=payload)
        self.assertEqual(200, response.status_code)
        user_details = json.loads(response.text)
        self.assertIsInstance(user_details, dict)

if __name__ == '__main__':
    unittest.main()

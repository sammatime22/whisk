'''
This file tests the Rest Client class, its methods and other relevant things, such that it works as intended.

sammatime22, 2021
'''
# Get the path to the display module (note as this baseline is so small, 
# this is to be run in the home dir of the project).
import sys
sys.path.append('src')

import unittest
from unittest.mock import patch
from rest_client import RestClient


class TestRestClient(unittest.TestCase):
    '''
    A set of tests for the Rest Client class.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''
    # A sample test FROM query portion
    test_sample_from_portion = "[\"Ice Cream\"]"

    # A sample test SELECT query portion
    test_sample_select_portion = "[[\"Flavor\", \"is\", \"Death by Chocolate\"]]"

    # A sample test INSERT query portion
    test_sample_insert_portion = "[[\"Flavor\"=\"Mint Chocolate Chip\", \"Price\"=2.00]]"

    # A sample test UPDATE query portion
    test_sample_update_portion = "[[\"Price\", \"to\", 1.00]]"

    # This rest client just has the default settings - no need to get fancy
    test_rest_client = RestClient()


    def test_01_successful_get(self):
        '''
        Tests the GET request when successful.
        '''

        # Patch the requests library
        with patch("requests.get") as mock_request:
            # Get the mocking set up
            mock_request.return_value.status_code = 200
            mock_request.return_value.content = "[[\"Flavor\"=\"Death by Chocolate\", \"Price\"=2.00]]"

            # Run the request
            success, response = \
                self.test_rest_client.get_request(self.test_sample_from_portion, self.test_sample_select_portion)

            # Test that the request contents came back as expected
            assert success == True
            assert response.status_code == 200
            assert response.content == "[[\"Flavor\"=\"Death by Chocolate\", \"Price\"=2.00]]"


    def test_02_unsuccessful_get(self):
        '''
        Tests the GET request when unsuccessful.
        '''
        with patch("requests.get") as mock_request:
            # Get the mocking set up
            mock_request.return_value.status_code = 404
            mock_request.return_value.content = ""

            # Run the request
            success, response = \
                self.test_rest_client.get_request(self.test_sample_from_portion, self.test_sample_select_portion)

            # Test that the request contents came back as expected
            assert success == True
            assert response.status_code == 404
            assert response.content == ""
     


    def test_03_connection_error_get(self):
        '''
        Tests the GET request with a connection error.
        '''
        # Try making the request, but with a bad url
        bad_rest_client = RestClient("http://", "255.255.255.255", "22")
        success, response = \
            self.test_rest_client.get_request(self.test_sample_from_portion, self.test_sample_select_portion)

        # Test that the request contents came back as expected
        assert success == False
        assert response ==  "A connection error has occured."


    def test_04_unknown_exception_get(self):
        '''
        Tests the GET request with an unknown error
        '''
        bad_rest_client = RestClient(RestClient(), 2, 3)
        success, response = \
            bad_rest_client.get_request(self.test_sample_from_portion, self.test_sample_select_portion)

        # Test that the request contents came back as expected
        assert success == False
        assert response ==  "An unidentified error has occured: unsupported operand type(s) for +: 'RestClient' and 'int'."

    def test_05_successful_post(self):
        '''
        Tests the POST request when successful.
        '''


    def test_06_unsuccessful_post(self):
        '''
        Tests the POST request when unsuccessful.
        '''


    def test_07_connection_error_post(self):
        '''
        Tests the POST request with a connection error.
        '''


    def test_08_unknown_exception_post(self):
        '''
        Tests the POST request with an unknown error
        '''


    def test_09_successful_update(self):
        '''
        Tests the UPDATE request when successful.
        '''


    def test_10_unsuccessful_update(self):
        '''
        Tests the UPDATE request when unsuccessful.
        '''


    def test_11_connection_error_update(self):
        '''
        Tests the UPDATE request with a connection error.
        '''


    def test_12_unknown_exception_update(self):
        '''
        Tests the UPDATE request with an unknown error
        '''


    def test_13_successful_delete(self):
        '''
        Tests the DELETE request when successful.
        '''


    def test_14_unsuccessful_delete(self):
        '''
        Tests the DELETE request when unsuccessful.
        '''


    def test_15_connection_error_delete(self):
        '''
        Tests the DELETE request with a connection error.
        '''


    def test_16_unknown_exception_delete(self):
        '''
        Tests the DELETE request with an unknown error
        '''
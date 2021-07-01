'''
This file tests the Rest Client class, its methods and other relevant things, such that it works as intended.

sammatime22, 2021
'''
# Get the path to the display module (note as this baseline is so small, 
# this is to be run in the home dir of the project).
import sys
sys.path.append('src')

import unittest
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


    def test_01_successful_get():
        '''
        Tests the GET request when successful.
        '''
        # Run the Query
        # Check that the parameters provided are right
        # Make sure the request looks right
        # Make sure we were "successful" in the eyes of the Rest Client
        # Make sure that as mocked, the response is good

    def test_02_unsuccessful_get():
        '''
        Tests the GET request when unsuccessful.
        '''
        # Run the Query
        # Check that the parameters provided are right
        # Make sure the request looks right
        # Make sure we were "successful" in the eyes of the Rest Client
        # Make sure that as mocked, the response is bad

    def test_03_connection_error_get():
        '''
        Tests the GET request with a connection error.
        '''
        # Run the Query
        # Check that the parameters provided are right
        # Make sure the request looks right
        # Make sure we were "unsuccessful" in the eyes of the Rest Client for a connnection error

    def test_04_unknown_exception_get():
        '''
        Tests the GET request with an unknown error
        '''
        # Run the Query
        # Check that the parameters provided are right
        # Make sure the request looks right
        # Make sure we were "unsuccessful" in the eyes of the Rest Client for an unexplained error

    def test_05_successful_post():
        '''
        Tests the POST request when successful.
        '''


    def test_06_unsuccessful_post():
        '''
        Tests the POST request when unsuccessful.
        '''


    def test_07_connection_error_post():
        '''
        Tests the POST request with a connection error.
        '''


    def test_08_unknown_exception_post():
        '''
        Tests the POST request with an unknown error
        '''


    def test_09_successful_update():
        '''
        Tests the UPDATE request when successful.
        '''


    def test_10_unsuccessful_update():
        '''
        Tests the UPDATE request when unsuccessful.
        '''


    def test_11_connection_error_update():
        '''
        Tests the UPDATE request with a connection error.
        '''


    def test_12_unknown_exception_update():
        '''
        Tests the UPDATE request with an unknown error
        '''


    def test_13_successful_delete():
        '''
        Tests the DELETE request when successful.
        '''


    def test_14_unsuccessful_delete():
        '''
        Tests the DELETE request when unsuccessful.
        '''


    def test_15_connection_error_delete():
        '''
        Tests the DELETE request with a connection error.
        '''


    def test_16_unknown_exception_delete():
        '''
        Tests the DELETE request with an unknown error
        '''
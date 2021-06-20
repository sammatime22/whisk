'''
This file tests the Display class, its methods and other relevant things, such that it works as intended.

sammatime22, 2021
'''
import unittest
from display import Display


class TestDisplay(unittest.TestCase):
    '''
    A set of tests for the Display class.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''


    # Just repeating the general three color constants
    RED = "\033[91m{}\033[00m"
    GREEN = "\033[92m{}\033[00m"
    BLUE = "\033[96m{}\033[00m"


    # The positions of the colors in the "color_choices" selection
    RED_POS = 0
    GREEN_POS = 1
    BLUE_POS = 2


    # A test message for us to use
    test_message = "Hello World!"


    # Just to set up an object - might not need a full setUpClass method for now
    test_whisk_display = Display()


    def test_print_success(self):
        '''
        Tests the print_success method for usage.
        '''
        self.test_whisk_display.print_success(test_message)


    def test_print_error(self):
        '''
        Tests the print_error method for usage.
        '''
        self.test_whisk_display.print_error(test_message)


    def test_print_general(self):
        '''
        Tests the print_general method for usage.
        '''
        self.test_whisk_display.print_general(test_message)


    def test_configure(self):
        '''
        Tests the configure method, then the print_success, print_error, and print_general methods.
        '''
        # Reconfigure the colors in use
        self.test_whisk_display.configure(RED_POS, BLUE_POS, GREEN_POS)

        # Test the different print methods
        self.test_whisk_display.print_success(test_message)
        self.test_whisk_display.print_error(test_message)
        self.test_whisk_display.print_general(test_message)
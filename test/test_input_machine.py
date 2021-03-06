'''
This file tests the Input Machine class, its methods and other relevant things, such that it works as intended.

sammatime22, 2021
'''
# Get the path to the display module (note as this baseline is so small, 
# this is to be run in the home dir of the project).
import sys
sys.path.append('src')

import unittest
from unittest.mock import patch, call
from input_machine import InputMachine


class TestInputMachine(unittest.TestCase):
    '''
    A set of tests for the Input Machine class.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''

    # The input machine for test
    test_input_machine = InputMachine()

    # A test input string
    what_can_i_get_you = "What can I get for you?"

    # The default pointer char
    pointer_char = ">"


    def test_01_successful_gather_input(self):
        '''
        Tests the gather_input method for successful usage. We check to see that the method returns our 
        mocked value, as well as that the input method within gather_input was called with the correct
        string.
        '''
        with patch('builtins.input') as mock_input:
            mock_input.return_value = 1234  # A fake value to return
            contents = self.test_input_machine.gather_input(self.what_can_i_get_you)
            assert mock_input.mock_calls == [call('{} {}'.format(self.what_can_i_get_you, self.pointer_char))]
            assert contents == 1234


    def test_02_unsuccessful_gather_input(self):
        '''
        Checks that on an unsuccessful gathering that None is returned.
        '''
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [Exception]  # We will set a side effect for the mock input to be an exception
            contents = self.test_input_machine.gather_input(self.what_can_i_get_you)
            assert contents == None

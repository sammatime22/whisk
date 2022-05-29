'''
This file tests the Bootloader and whatever methods are associated to that.

sammatime22, 2022
'''
import sys
sys.path.append('src')

import unittest 
from unittest.mock import patch, call
from bootloader import kickstart, WELCOME
from display import Display
from input_machine import InputMachine
from rest_client import RestClient

class TestBootloader(unittest.TestCase):
    '''
    A set of tests for the Bootloader.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''

    # A mock Display object for test
    test_whisk_display = Display()

    # A mock Input Machine for test
    test_input_machine = InputMachine()

    # A mock Rest Client for test
    test_rest_client = RestClient()

    # Tests for Kickstart
    def test_1_kickstart(self):
        '''
        This test checks that the kickstart method would run without error.
        '''
        # Just providing the return of three values for the 
        # get_protocol_host_port method.
        def side_effect_method_protocol():
            return None, None, None

        # Again, another method that is a side effect fill in that does nothing
        def side_effect_start_engine(display, rest_client, input_machine):
            return None

        with patch('display.Display.print_general') as mock_print_general:
            with patch('rest_client.RestClient.get_protocol_host_port') as mock_get_protocol_host_port:
                with patch('threading.Thread.start') as mock_start_engine:
                    # Apply the side effect methods and kickstart the engine
                    mock_get_protocol_host_port.side_effect = side_effect_method_protocol
                    mock_start_engine.side_effect = side_effect_start_engine(self.test_whisk_display, self.test_rest_client, self.test_input_machine)
                    kickstart([])

                    # Assert that the print general was called w/the welcome message,
                    # as well as the mock calls to gather the socket info and run the engine
                    assert mock_print_general.mock_calls.count(call(WELCOME)) == 1
                    assert len(mock_get_protocol_host_port.mock_calls) == 1
                    assert len(mock_start_engine.mock_calls) == 1

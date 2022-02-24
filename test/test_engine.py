'''
This file tests the workings of the Whisk engine, that it operates accordingly under given inputs

sammatime22, 2021-2022
'''
import sys
sys.path.append('src')

import unittest
from unittest.mock import patch, call
from engine import Engine
from display import Display
from input_machine import InputMachine

class TestEngine(unittest.TestCase):
    '''
    A set of test for the Engine class.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''

    # A mock Engine object for test
    test_engine = Engine()

    # A mock Display object for test
    test_whisk_display = Display()

    # A mock Input Machine for test
    test_input_machine = InputMachine()

    # Tests for Retrieve Command
    def test_01_retrieve_command_successful(self):
        '''
        Tests that the retrieve command is successful.
        '''
        with patch('builtins.print') as mock_print:
            please_provide = "\nPlease provide one of the following:\nGET, POST, UPDATE, DELETE, HELP, EXIT"
            not_case_sensitive = "Do note that this is not case sensitive."
            self.test_engine.retrieve_command(self.test_whisk_display, self.test_input_machine)
            assert len(mock_print.mock_calls) == 2 # [please_provide, not_case_sensitive]


    def test_02_retrieve_command_exception_handled(self):
        '''
        Tests that the retrieve command can handle exceptions.
        '''


    # Tests for Help Command
    def test_03_help_command_get(self):
        '''
        Tests the proper output from the GET command's help output.
        '''


    def test_04_help_command_post(self):
        '''
        Tests the proper output from the POST command's help output.
        '''


    def test_05_help_command_update(self):
        '''
        Tests the proper output from the UPDATE command's help output.
        '''


    def test_06_help_command_delete(self):
        '''
        Tests the proper output from the DELETE command's help output.
        '''


    def test_07_help_command_help(self):
        '''
        Tests the proper output from the HELP command's help output.
        '''


    def test_08_help_command_exit(self):
        '''
        Tests the proper output from the EXIT command's help output.
        '''


    def test_09_help_command_exception_handling(self):
        '''
        Tests the help command has proper exception handling.
        '''


    # Tests for Get Command
    def test_10_get_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful GET request.
        '''


    def test_11_get_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful GET request.
        '''


    def test_12_get_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous GET request.
        '''


    def test_13_get_command_exception_handled(self):
        '''
        Tests the get_command can properly handle exceptions.
        '''


    # Tests for Post Command
    def test_14_post_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful POST request.
        '''


    def test_15_post_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful POST request.
        '''


    def test_16_post_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous POST request.
        '''


    def test_17_post_command_exception_handled(self):
        '''
        Tests the post_command can properly handle exceptions.
        '''


    # Tests for Update Command
    def test_18_update_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful UPDATE request.
        '''


    def test_19_update_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful UPDATE request.
        '''


    def test_20_update_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous UPDATE request.
        '''


    def test_21_update_command_exception_handled(self):
        '''
        Tests the update_command can properly handle exceptions.
        '''


    # Tests for Delete Command
    def test_22_delete_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful DELETE request.
        '''


    def test_23_delete_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful DELETE request.
        '''


    def test_24_delete_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous DELETE request.
        '''


    def test_25_delete_command_exception_handled(self):
        '''
        Tests the delete_command can properly handle exceptions.
        '''


    # Tests for Run Engine
    def test_26_run_engine_get_command_called(self):
        '''
        Tests that when GET is provided, that get_command is called.
        '''


    def test_27_run_engine_post_command_called(self):
        '''
        Tests that when POST is provided, that post_command is called.
        '''


    def test_28_run_engine_update_command_called(self):
        '''
        Tests that when UPDATE is provided, that update_command is called.
        '''


    def test_29_run_engine_delete_command_called(self):
        '''
        Tests that when DELETE is provided, that delete_command is called.
        '''

    def test_30_run_engine_help_command_called(self):
        '''
        Tests that when HELP is provided, that help_command is called.
        '''


    def test_31_run_engine_exit_command_called(self):
        '''
        Tests that when EXIT is provided, that no actions are further called.
        '''


    def test_32_run_engine_exception_handling(self):
        '''
        Tests that the run_engine method can properly handle errors.
        '''


    # Tests for Kickstart
    def test_33_kickstart(self):
        '''
        This test checks that the kickstart method would run without error.
        '''

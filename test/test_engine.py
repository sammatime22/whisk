'''
This file tests the workings of the Whisk engine, that it operates accordingly under given inputs

sammatime22, 2021-2022
'''



class TestEngine(unittest.TestCase):
    '''
    A set of test for the Engine class.

    Parameters
    ----------
    unittest.TestCase : from unittest dependency
        Provides the Unit Test functionality for the class
    '''

    # Tests for Retrieve Command
    def test_retrieve_command_successful():
        '''
        Tests that the retrieve command is successful.
        '''


    def test_retrieve_command_exception_handled():
        '''
        Tests that the retrieve command can handle exceptions.
        '''


    # Tests for Help Command
    def test_help_command_get():
        '''
        Tests the proper output from the GET command's help output.
        '''


    def test_help_command_post():
        '''
        Tests the proper output from the POST command's help output.
        '''


    def test_help_command_update():
        '''
        Tests the proper output from the UPDATE command's help output.
        '''


    def test_help_command_delete():
        '''
        Tests the proper output from the DELETE command's help output.
        '''


    def test_help_command_help():
        '''
        Tests the proper output from the HELP command's help output.
        '''


    def test_help_command_exit():
        '''
        Tests the proper output from the EXIT command's help output.
        '''


    def test_help_command_exception_handling():
        '''
        Tests the help command has proper exception handling.
        '''


    # Tests for Get Command
    def test_get_command_successful():
        '''
        Tests the proper output is displayed upon a successful GET request.
        '''


    def test_get_command_unsuccessful():
        '''
        Tests the proper output is displayed upon an unsuccessful GET request.
        '''


    def test_get_command_erroneous():
        '''
        Tests the proper output is displayed upon an erroneous GET request.
        '''


    def test_get_command_exception_handled():
        '''
        Tests the get_command can properly handle exceptions.
        '''


    # Tests for Post Command
    def test_post_command_successful():
        '''
        Tests the proper output is displayed upon a successful POST request.
        '''


    def test_post_command_unsuccessful():
        '''
        Tests the proper output is displayed upon an unsuccessful POST request.
        '''


    def test_post_command_erroneous():
        '''
        Tests the proper output is displayed upon an erroneous POST request.
        '''


    def test_post_command_exception_handled():
        '''
        Tests the post_command can properly handle exceptions.
        '''


    # Tests for Update Command
    def test_update_command_successful():
        '''
        Tests the proper output is displayed upon a successful UPDATE request.
        '''


    def test_update_command_unsuccessful():
        '''
        Tests the proper output is displayed upon an unsuccessful UPDATE request.
        '''


    def test_update_command_erroneous():
        '''
        Tests the proper output is displayed upon an erroneous UPDATE request.
        '''


    def test_update_command_exception_handled():
        '''
        Tests the update_command can properly handle exceptions.
        '''


    # Tests for Delete Command
    def test_delete_command_successful():
        '''
        Tests the proper output is displayed upon a successful DELETE request.
        '''


    def test_delete_command_unsuccessful():
        '''
        Tests the proper output is displayed upon an unsuccessful DELETE request.
        '''


    def test_delete_command_erroneous():
        '''
        Tests the proper output is displayed upon an erroneous DELETE request.
        '''


    def test_delete_command_exception_handled():
        '''
        Tests the delete_command can properly handle exceptions.
        '''


    # Tests for Run Engine
    def test_run_engine_get_command_called():
        '''
        Tests that when GET is provided, that get_command is called.
        '''


    def test_run_engine_post_command_called():
        '''
        Tests that when POST is provided, that post_command is called.
        '''


    def test_run_engine_update_command_called():
        '''
        Tests that when UPDATE is provided, that update_command is called.
        '''


    def test_run_engine_delete_command_called():
        '''
        Tests that when DELETE is provided, that delete_command is called.
        '''

    def test_run_engine_help_command_called():
        '''
        Tests that when HELP is provided, that help_command is called.
        '''


    def test_run_engine_exit_command_called():
        '''
        Tests that when EXIT is provided, that no actions are further called.
        '''


    def test_run_engine_exception_handling():
        '''
        Tests that the run_engine method can properly handle errors.
        '''


    # Tests for Kickstart
    def test_kickstart():
        '''
        This test checks that the kickstart method would run without error.
        '''

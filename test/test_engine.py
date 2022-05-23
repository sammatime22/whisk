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
from rest_client import RestClient

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

    # A mock Rest Client for test
    test_rest_client = RestClient()

    # A mocked Response class for tests
    class MockResponse():
        '''
        Again, a mock class for Responses over REST.
        '''

        # The status code of the response (HTTP 200, 404, etc.)
        status_code = 0

        # The content of the response
        content = None

        # The constructor for the mock Response object
        def __init__(self, status_code, content):
            self.status_code = status_code
            self.content = content



    # Tests for Retrieve Command
    def test_01_retrieve_command_successful(self):
        '''
        Tests that the retrieve command is successful.
        '''
        # Set up the commands and expected print statements
        test_command = "GET"
        please_provide = "\nPlease provide one of the following:\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "Do note that this is not case sensitive."
        your_command = "Your Command"

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned value from the input machine, and call the retrieve_command method
                mock_gather_input.return_value = test_command
                retrieved_command = self.test_engine.retrieve_command(self.test_whisk_display, self.test_input_machine)
                
                # Assess the expected calls were made within the method, and that we got the correct return value
                assert mock_print_general.mock_calls == [call(please_provide), call(not_case_sensitive)]
                assert mock_gather_input.mock_calls == [call(your_command)]
                assert retrieved_command == test_command


    def test_02_retrieve_command_exception_handled(self):
        '''
        Tests that the retrieve command can handle exceptions.
        '''
        # Set up the commands and expected print statements
        please_provide = "\nPlease provide one of the following:\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "Do note that this is not case sensitive."
        your_command = "Your Command"
        unrecognized_value = "An unrecognized value was provided."
        skip = "SKIP"

        # Mock the general printing, error printing, and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                    # Mock the returned value from the input machine, and call the retrieve_command method
                    mock_gather_input.return_value = None
                    retrieved_command = self.test_engine.retrieve_command(self.test_whisk_display, self.test_input_machine)
                    
                    # Assess the expected calls were made within the method, and that we got the correct return value
                    assert mock_print_general.mock_calls == [call(please_provide), call(not_case_sensitive)]
                    assert mock_print_error.mock_calls == [call(unrecognized_value)]
                    assert mock_gather_input.mock_calls == [call(your_command)]
                    assert retrieved_command == skip


    # Tests for Help Command
    def test_03_help_command_get(self):
        '''
        Tests the proper output from the GET command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "GET"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"
        # Just to further organize, these are the expected "print" statements
        get_command_info_one = "This command allows users to retrieve data from the DB."
        get_command_info_two = "Below are the promts provided with the GET command:"
        get_command_info_three = "From: Provide the name of the table in the database you would like data from."
        get_command_info_four = "Select: A query of format \"key\" \"operation\" \"value\", given over three inputs."

        # Mock the general printing and the input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(get_command_info_one),\
                                                        call(get_command_info_two), call(get_command_info_three), call(get_command_info_four)]
                assert mock_gather_input.mock_calls == [call(gather_info_on)]


    def test_04_help_command_post(self):
        '''
        Tests the proper output from the POST command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "POST"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        post_command_info_one = "This command allows users to insert data into the DB."
        post_command_info_two = "Below are the promts provided with the POST command:"
        post_command_info_three = "From: Provide the name of the table in the database you would like to insert data."
        post_command_info_four = "Select: A query of format \"key\" \"operation\" \"value\", given over three inputs."
        post_command_info_five = "Insert: An item to insert, in key-value pairs provided in 2D arrays in one 2D array"

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(post_command_info_one), \
                    call(post_command_info_two), call(post_command_info_three), call(post_command_info_four), call(post_command_info_five)]
                assert mock_gather_input.mock_calls == [call(gather_info_on)]


    def test_05_help_command_update(self):
        '''
        Tests the proper output from the UPDATE command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "UPDATE"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        update_command_info_one = "This command allows users to update data in the DB."
        update_command_info_two = "Below are the promts provided with the UPDATE command:"
        update_command_info_three = "From: Provide the name of the table in the database you would like to update."
        update_command_info_four = "Select: A query of format \"key\" \"operation\" \"value\", given over three inputs"
        update_command_info_five = "Update: An update action of format \"key\" \"operation\" \"value\" in three inputs"

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(update_command_info_one),\
                    call(update_command_info_two), call(update_command_info_three), call(update_command_info_four), call(update_command_info_five)]
                assert mock_gather_input.mock_calls  == [call(gather_info_on)]


    def test_06_help_command_delete(self):
        '''
        Tests the proper output from the DELETE command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "DELETE"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        delete_command_info_one = "This command allows users to remove data from the DB."
        delete_command_info_two = "Below are the promts provided with the DELETE command:"
        delete_command_info_three = "From: Provide the name of the table in the database you would remove data from."
        delete_command_info_four = "Select: A query of format \"key\" \"operation\" \"value\", given over three inputs"

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(delete_command_info_one),\
                        call(delete_command_info_two), call(delete_command_info_three), call(delete_command_info_four)]
                assert mock_gather_input.mock_calls == [call(gather_info_on)]


    def test_07_help_command_help(self):
        '''
        Tests the proper output from the HELP command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "HELP"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        help_command_info = "After typing help in any casing, when prompted, provide the command of interest."

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(help_command_info)]
                assert mock_gather_input.mock_calls == [call(gather_info_on)]


    def test_08_help_command_exit(self):
        '''
        Tests the proper output from the EXIT command's help output.
        '''
        # Set up the commands and expected print statements
        test_command = "EXIT"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        exit_command_info = "Just simply type exit when promted in any casing and you will exit the app."

        # Mock the general printing and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                # Mock the returned input from the input machine, and call the help command
                mock_gather_input.return_value = test_command
                self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                # Assess the expected calls were made within the method
                assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive), call(exit_command_info)]
                assert mock_gather_input.mock_calls == [call(gather_info_on)]


    def test_09_help_command_unrecognized_input(self):
        '''
        Tests the help command handles unrecognized commands accordingly.
        '''
        # Set up the commands and expected print statements
        test_command = "just an incoherent command"
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        command_provided_unrecognized = "The command provided was not recognized"

        # Mock the general printing, error printing, and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                with patch('display.Display.print_error') as mock_print_error:
                    # Mock the returned input from the input machine, and call the help command
                    mock_gather_input.return_value = test_command
                    self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                    # Assess the expected calls were made within the method
                    assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive)]
                    assert mock_gather_input.mock_calls == [call(gather_info_on)]
                    assert mock_print_error.mock_calls == [call(command_provided_unrecognized)]


    def test_10_help_command_exception_handling(self):
        '''
        Tests the help command has proper exception handling.

        NOTE that we are already handling the exception one class above, and this is merely to assert
        we are not running unrecognized commands.
        '''
        # Set up the commands and expected print statements
        test_command = None
        what_command = "What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT"
        not_case_sensitive = "This is not case sensitive."
        gather_info_on = "Gather Info On"

        # Assign the expected print statements to variables
        error_seen_gathering_input = "An error was seen when gathering the command of interest"

        # Mock the general printing, error printing, and input gathering
        with patch('display.Display.print_general') as mock_print_general:
            with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
                with patch('display.Display.print_error') as mock_print_error:
                    # Mock the returned input from the input machine, and call the help command
                    mock_gather_input.return_value = test_command
                    self.test_engine.help_command(self.test_whisk_display, self.test_input_machine)

                    # Assess the expected calls were made within the method
                    assert mock_print_general.mock_calls == [call(what_command), call(not_case_sensitive)]
                    assert mock_gather_input.mock_calls == [call(gather_info_on)]
                    assert mock_print_error.mock_calls == [call(error_seen_gathering_input)]


    # Tests for Get Command
    def test_11_get_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful GET request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Electrical Components"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Item"
        select_operation_portion = "is"
        select_value_portion = "LED"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"

        # Provide what we expect following a successful GET request
        retrieved = True
        status_code = 200
        content = "b'[{Item=LED, Price=$0.79}]'"

        # Make an object to hold the response
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion

        def side_effect_method_get(from_portionn, select_portionn):
            if from_portionn == from_portion_full and select_portionn == select_portion_full:
                return True, mock_response
            else:
                return False, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_success') as mock_print_success:
                with patch('rest_client.RestClient.get_request') as mock_get_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_get_request.side_effect = side_effect_method_get
                    self.test_engine.get_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_success.mock_calls.count(call(str(mock_response.status_code) + " : " + str(mock_response.content))) == 1


    def test_12_get_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful GET request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Electrical Components"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Name"
        select_operation_portion = "is"
        select_value_portion = "Ice Cream"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        
        # Provide what we expect following an unsuccessful GET request
        retrieved = False
        status_code = 404
        content = ""

        # Make an object to hold the response
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion

        def side_effect_method_get(from_portionn, select_portionn):
            if from_portionn == from_portion_full and select_portionn == select_portion_full:
                return True, mock_response
            else:
                return False, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.get_request') as mock_get_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_get_request.side_effect = side_effect_method_get
                    self.test_engine.get_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(str(mock_response.status_code) + " : " + str(mock_response.content))) == 1


    def test_13_get_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous GET request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Electrical Components"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Item Name"
        select_operation_portion = "is"
        select_value_portion = "LED"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"

        # Provide what we expect following a failed GET request
        retrieved = False
        error_message = "A connection error has occurred."

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion

        def side_effect_method_get(from_portionn, select_portionn):
            return False, error_message

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('rest_client.RestClient.get_request') as mock_get_request:
                with patch('display.Display.print_error') as mock_print_error:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_get_request.side_effect = side_effect_method_get
                    self.test_engine.get_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(error_message)) == 1


    def test_14_get_command_exception_handled(self):
        '''
        Tests the get_command can properly handle exceptions.
        '''
        # Mock the input gathering, error display
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                # Cause the gather input method to immediately throw an exception
                mock_gather_input.side_effect = [Exception]
                self.test_engine.get_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)
                
                # See that the appropriate methods were called an appropriate amount of times
                assert mock_gather_input.mock_calls.count(call("From")) == 1
                assert len(mock_print_error.mock_calls) == 1


    # Tests for Post Command
    def test_15_post_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful POST request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        insert = "Insert"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Plates"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Material"
        select_operation_portion = "is"
        select_value_portion = "Metal"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        insert_portion_full = "{\"Name\": \"SilverPlatter\", \"Price\": 10.00, \"Currency\": \"$\"}"

        # Provide what we expect following a successful POST request
        retrieved = True
        status_code = 201
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt): 
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == insert:
                return insert_portion_full

        def side_effect_method_post(from_portionn, select_portionn, insert_portionn): 
            if (from_portionn == from_portion_full) and \
                (select_portionn == select_portion_full) and \
                (insert_portionn == insert_portion_full):
                return retrieved, mock_response
            else:
                False, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_success') as mock_print_success:
                with patch('rest_client.RestClient.post_request') as mock_post_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_post_request.side_effect = side_effect_method_post
                    self.test_engine.post_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(insert)) == 1

                    # Assert the proper values were returned
                    assert mock_print_success.mock_calls.count(call(str(mock_response.status_code) + " : " + str(mock_response.content))) == 1
   

    def test_16_post_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful POST request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        insert = "Insert"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Magnets"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Strength (A/m)"
        select_operation_portion = ">"
        select_value_portion = "10"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        insert_portion_full = "{\"Name\": \"My Mag\"}"

        # Provide what we expect following an unsuccessful POST request
        retrieved = True
        status_code = 409
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == insert:
                return insert_portion_full


        def side_effect_method_post(from_portionn, select_portionn, insert_portionn):
            if (from_portionn == from_portion_full) and \
                (select_portionn == select_portion_full) and\
                (insert_portionn == insert_portion_full):
                return retrieved, mock_response
            else:
                return False, None

         

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.post_request') as mock_post_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_post_request.side_effect = side_effect_method_post
                    self.test_engine.post_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(insert)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(str(mock_response.status_code) + " : " + str(mock_response.content))) == 1
  

    def test_17_post_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous POST request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        insert = "Insert"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Sweaters"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = ""
        select_operation_portion = ""
        select_value_portion = ""
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        insert_portion_full = "{\"Name\": \"Too Comfy\"}"

        # Provide what we expect following an unsuccessful POST request
        retrieved = False
        error_message = "An unidentified error has occurred: Out Of Memory"

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == insert:
                return insert_portion_full

        def side_effect_method_post(from_portionn, select_portionn, insert_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full)\
                and (insert_portionn == insert_portion_full):
                return retrieved, error_message
            else:
                return not retrieved, error_message

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.post_request') as mock_post_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_post_request.side_effect = side_effect_method_post
                    self.test_engine.post_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(insert)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(error_message)) == 1
  

    def test_18_post_command_exception_handled(self):
        '''
        Tests the post_command can properly handle exceptions.
        '''
        # Mock the input gathering, error display
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                # Cause the gather input method to immediately throw an exception
                mock_gather_input.side_effect = [Exception]
                self.test_engine.post_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                # See that the appropriate methods were called an appropriate amount of times
                assert mock_gather_input.mock_calls.count(call("From")) == 1
                assert len(mock_print_error.mock_calls) == 1
 

    # Tests for Update Command
    def test_19_update_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful UPDATE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        update_key = "Update (key)"
        update_operation = "Update (operation)"
        update_value = "Update (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Books"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Author"
        select_operation_portion = "is"
        select_value_portion = "sammatime22"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        update_key_portion = "Recommendation"
        update_operation_portion = "to"
        update_value_portion = "true"
        update_portion_full = "[[\"" + update_key_portion + "\", \"" + update_operation_portion + "\", \"" + update_value_portion + "\"]]"

        # Provide what we expect following a successful UPDATE request
        retrieved = True
        status_code = 200
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == update_key:
                return update_key_portion
            elif input_prompt == update_operation:
                return update_operation_portion
            elif input_prompt == update_value:
                return update_value_portion

        def side_effect_method_update(from_portionn, select_portionn, update_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full)\
                and (update_portionn == update_portion_full):
                return retrieved, mock_response
            else:
                return not retrieved, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_success') as mock_print_success:
                with patch('rest_client.RestClient.update_request') as mock_update_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_update_request.side_effect = side_effect_method_update
                    self.test_engine.update_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_success.mock_calls.count(call(str(status_code) + " : " + str(content))) == 1


    def test_20_update_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful UPDATE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        update_key = "Update (key)"
        update_operation = "Update (operation)"
        update_value = "Update (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Coffee"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Sauce"
        select_operation_portion = ">"
        select_value_portion = "headphones"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        update_key_portion = "price"
        update_operation_portion = "to"
        update_value_portion = "saucey"
        update_portion_full = "[[\"" + update_key_portion + "\", \"" + update_operation_portion + "\", \"" + update_value_portion + "\"]]"

        # Provide what we expect following an unsuccessful UPDATE request
        retrieved = True
        status_code = 409
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == update_key:
                return update_key_portion
            elif input_prompt == update_operation:
                return update_operation_portion
            elif input_prompt == update_value:
                return update_value_portion

        def side_effect_method_update(from_portionn, select_portionn, update_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full)\
                and (update_portionn == update_portion_full):
                return retrieved, mock_response
            else:
                return not retrieved, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.update_request') as mock_update_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_update_request.side_effect = side_effect_method_update
                    self.test_engine.update_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_key)) == 1 
                    assert mock_gather_input.mock_calls.count(call(update_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(str(status_code) + " : " + str(content))) == 1


    def test_21_update_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous UPDATE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"
        update_key = "Update (key)"
        update_operation = "Update (operation)"
        update_value = "Update (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Vegetables"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Name"
        select_operation_portion = "is"
        select_value_portion = "Carrots"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"
        update_key_portion = "Price"
        update_operation_portion = "is"
        update_value_portion = "$4"
        update_portion_full = "[[\"" + update_key_portion + "\", \"" + update_operation_portion + "\", \"" + update_value_portion + "\"]]"

        # Provide what we expect following an erroneous UPDATE request
        retrieved = False
        error_message = "A connection error has occurred."

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion
            elif input_prompt == update_key:
                return update_key_portion
            elif input_prompt == update_operation:
                return update_operation_portion
            elif input_prompt == update_value:
                return update_value_portion

        def side_effect_method_update(from_portionn, select_portionn, update_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full)\
                and (update_portionn == update_portion_full):
                return retrieved, error_message
            else:
                return not retrieved, ""

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.update_request') as mock_update_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_update_request.side_effect = side_effect_method_update
                    self.test_engine.update_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(update_value))

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(error_message)) == 1


    def test_22_update_command_exception_handled(self):
        '''
        Tests the update_command can properly handle exceptions.
        '''
        # Mock the input gathering, error display
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                # Cause the gather input method to immediately throw an exception
                mock_gather_input.side_effect = [Exception]
                self.test_engine.update_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                # See that the appropriate methods were called an appropriate amount of times
                assert mock_gather_input.mock_calls.count(call("From")) == 1
                assert len(mock_print_error.mock_calls) == 1


    # Tests for Delete Command
    def test_23_delete_command_successful(self):
        '''
        Tests the proper output is displayed upon a successful DELETE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Books"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Title"
        select_operation_portion = "is"
        select_value_portion = "Making Poke"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"

        # Provide what we expect following a successful DELETE request
        retrieved = True
        status_code = 204
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion

        def side_effect_method_delete(from_portionn, select_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full):
                return retrieved, mock_response
            else:
                return not retrieved, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_success') as mock_print_success:
                with patch('rest_client.RestClient.delete_request') as mock_delete_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_delete_request.side_effect = side_effect_method_delete
                    self.test_engine.delete_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_success.mock_calls.count(call(str(mock_response.status_code) + " : " + str(mock_response.content)))


    def test_24_delete_command_unsuccessful(self):
        '''
        Tests the proper output is displayed upon an unsuccessful DELETE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Milkshakes"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Flavor"
        select_operation_portion = "is"
        select_value_portion = "earpods"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"

        # Provide what we expect following an unsuccessful DELETE request
        retrieved = True
        status_code = 409
        content = ""
        mock_response = self.MockResponse(status_code, content)

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion


        def side_effect_method_delete(from_portionn, select_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full):
                return retrieved, mock_response
            else:
                return not retrieved, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.delete_request') as mock_delete_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_delete_request.side_effect = side_effect_method_delete
                    self.test_engine.delete_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(str(str(status_code) + " : " + str(content))))


    def test_25_delete_command_erroneous(self):
        '''
        Tests the proper output is displayed upon an erroneous DELETE request.
        '''
        # Provide the parameters we will use for the gather_input methods
        f_rom = "From"
        select_key = "Select (key)"
        select_operation = "Select (operation)"
        select_value = "Select (value)"

        # Provide what parameters we will mock that the user provides at the CLI
        from_portion = "Gogurt"
        from_portion_full = "[\"" + from_portion + "\"]"
        select_key_portion = "Price"
        select_operation_portion = ">"
        select_value_portion = "40.00"
        select_portion_full = "[[\"" + select_key_portion + "\", \"" + select_operation_portion + "\", \"" + select_value_portion + "\"]]"

        # Provide what we expect following an erroneous DELETE request
        retrieved = False
        response = "A connection error has occurred."

        # Define the "side effect" methods
        def side_effect_method_gather(input_prompt):
            if input_prompt == f_rom:
                return from_portion
            elif input_prompt == select_key:
                return select_key_portion
            elif input_prompt == select_operation:
                return select_operation_portion
            elif input_prompt == select_value:
                return select_value_portion

        def side_effect_method_delete(from_portionn, select_portionn):
            if (from_portionn == from_portion_full) and (select_portionn == select_portion_full):
                return retrieved, response
            else:
                return not retrieved, None

        # Mock the input machine, display, and rest client
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                with patch('rest_client.RestClient.delete_request') as mock_delete_request:
                    # Mock the return values and call the command
                    mock_gather_input.side_effect = side_effect_method_gather
                    mock_delete_request.side_effect = side_effect_method_delete
                    self.test_engine.delete_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                    # Assert the appropriate commands were provided to the appropriate methods
                    assert mock_gather_input.mock_calls.count(call(f_rom)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_key)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_operation)) == 1
                    assert mock_gather_input.mock_calls.count(call(select_value)) == 1

                    # Assert the proper values were returned
                    assert mock_print_error.mock_calls.count(call(response)) == 1


    def test_26_delete_command_exception_handled(self):
        '''
        Tests the delete_command can properly handle exceptions.
        '''
        # Mock the input gathering, error display
        with patch('input_machine.InputMachine.gather_input') as mock_gather_input:
            with patch('display.Display.print_error') as mock_print_error:
                # Cause the gather input method to immediately throw an exception
                mock_gather_input.side_effect = [Exception]
                self.test_engine.delete_command(self.test_whisk_display, self.test_rest_client, self.test_input_machine)

                # See that the appropriate methods were called an appropriate amount of times
                assert mock_gather_input.mock_calls.count(call("From")) == 1
                assert len(mock_print_error.mock_calls) == 1


    # Tests for Run Engine
    def test_27_run_engine_get_command_called(self):
        '''
        Tests that when GET is provided, that get_command is called.
        '''


    def test_28_run_engine_post_command_called(self):
        '''
        Tests that when POST is provided, that post_command is called.
        '''


    def test_29_run_engine_update_command_called(self):
        '''
        Tests that when UPDATE is provided, that update_command is called.
        '''


    def test_30_run_engine_delete_command_called(self):
        '''
        Tests that when DELETE is provided, that delete_command is called.
        '''

    def test_31_run_engine_help_command_called(self):
        '''
        Tests that when HELP is provided, that help_command is called.
        '''


    def test_32_run_engine_exit_command_called(self):
        '''
        Tests that when EXIT is provided, that no actions are further called.
        '''
        # just test that print_general is only called once


    # Tests for Kickstart
    def test_33_kickstart(self):
        '''
        This test checks that the kickstart method would run without error.
        '''
        # Just providing the return of three values for the 
        # get_protocol_host_port method.
        def side_effect_method_protocol():
            return None, None, None

        # Again, another method that is a side effect fill in that does nothing
        def side_effect_run_engine(display, rest_client, input_machine):
            return None

        with patch('display.Display.print_general') as mock_print_general:
            with patch('rest_client.RestClient.get_protocol_host_port') as mock_get_protocol_host_port:
                with patch('engine.Engine.run_engine') as mock_run_engine:
                    # Apply the side effect methods and kickstart the engine
                    mock_get_protocol_host_port.side_effect = side_effect_method_protocol
                    mock_run_engine.side_effect = side_effect_run_engine
                    self.test_engine.kickstart()

                    # Assert that the print general was called w/the welcome message,
                    # as well as the mock calls to gather the socket info and run the engine
                    assert mock_print_general.mock_calls.count(call(self.test_engine.WELCOME)) == 1
                    assert len(mock_get_protocol_host_port.mock_calls) == 1
                    assert len(mock_run_engine.mock_calls) == 1

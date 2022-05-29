

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

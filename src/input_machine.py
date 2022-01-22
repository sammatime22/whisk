'''
Helps to facilitate better console input for the Whisk application.

sammatime22, 2021
'''
import readline # Used for Arrow Keys (up-down->history, left-right->cursor)

class InputMachine:
    '''
    A singleton used to provide input capabilities, interpreting the input at the CLI
    '''


    # The character used to define where the input is going to be placed
    pointer_char = ">"


    # The general format for the input CLI statements
    input_format = "{} {}"


    def __init__(self, pointer_char = None):
        '''
        This constructor takes an optional parameter of a pointer char, so the application can
        be configured with a different char to show where the input should be placed.

        Parameters:
        ----------
        pointer_char (optional) : string
            The optional parameter that can override the pointer character used by the Input
            Machine to designate where the input will go on the CLI.
        '''
        if pointer_char is not None:
            self.pointer_char = pointer_char


    
    def gather_input(self, input_text):
        '''
        This constructor takes an optional parameter of a pointer char, so the application can
        be configured with a different char to show where the input should be placed.

        Parameters:
        ----------
        input_text : string
            The text presented to the user to provide info on what text they are about to provide.

        Return
        ----------
        contents : any, None on failure
            The contents retrieved at the CLI, where if a failure occurs None will be returned.
        '''
        try:
            contents = input(self.input_format.format(input_text, self.pointer_char))
            return contents
        except Exception as e:
            return None


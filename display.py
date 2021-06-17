'''
This class helps to facilitate better console output for the Whisk application.

sammatime22
'''

class Display:
    '''
    A singleton used to provide output capabilities, formatting content into colors, etc.
    '''

    # Color class constants
    RED = "\033[91m{}\033[00m"
    GREEN = "\033[92m{}\033[00m"
    BLUE = "\033[96m{}\033[00m"


    # Color-Descriptive relation
    success = GREEN
    error = RED
    general = BLUE

    def __init__(self):
        '''
        An initializer for the display.
        '''
        self.print_success("Display Initialized...")


    def __init__(self, success_color_choice, error_color_choice, general_color_choice):
        '''
        An initializer type that allows the user to choose which colors they want for each description type.
        '''

    def print_success(self, content):
        '''
        Prints the provided contents with a GREEN highlighting, indicating success.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.success.format(content))


    def print_error(self, content):
        '''
        Prints the provided contents with a RED highlighting, indicating failure.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.error.format(content))


    def print_general(self, content):
        '''
        Prints the provided contents with a BLUE highlighting, for general use.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.general.format(content))

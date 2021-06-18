'''
This class helps to facilitate better console output for the Whisk application.

sammatime22
'''
from enum import Enum

class ColorEnum(Enum):
    '''
    An enum class used to define colors for the Display class for instantiation
    '''
    RED = 0
    GREEN = 1
    BLUE = 2

class Display:
    '''
    A singleton used to provide output capabilities, formatting content into colors, etc.
    '''

    # Color class constants
    RED = "\033[91m{}\033[00m"
    GREEN = "\033[92m{}\033[00m"
    BLUE = "\033[96m{}\033[00m"

    # Color array to use for customized instantiation of the Display class
    color_choices = [RED, GREEN, BLUE]

    # Color-Descriptive relation defaults
    success = GREEN
    error = RED
    general = BLUE

    def __init__(self):
        '''
        An initializer for the display.
        '''
        self.print_success("Display Initialized...")


    def configure(self, success_color_choice, error_color_choice, general_color_choice):
        '''
        A configure method that allows the user to choose which colors they want for each description type.

        Parameters
        ----------
        success_color_choice : int
            An integer defining the color choice for success messages
        error_color_choice : int
            An integer defining the color choice for error messages
        general_color_choice : int
            An integer defining the color choice for general messages
        '''
        self.success = color_choices[success_color_choice]
        self.error = color_choices[error_color_choice]
        self.general = color_choices[general_color_choice]

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

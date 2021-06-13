'''
This class helps to facilitate better console output for the Whisk application.

sammatime22
'''

class Display:
    '''
    A singleton used to provide output capabilities, formatting content into colors, etc.
    '''

    red = "\033[91m{}\033[00m"
    green = "\033[92m{}\033[00m"
    blue = "\033[96m{}\033[00m"

    def __init__(self):
        '''
        An initializer for the display.
        '''
        self.print_success("Display Initialized...")


    def print_success(self, content):
        '''
        Prints the provided contents with a green highlighting, indicating success.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.green.format(content))


    def print_error(self, content):
        '''
        Prints the provided contents with a red highlighting, indicating failure.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.red.format(content))


    def print_general(self, content):
        '''
        Prints the provided contents with a blue highlighting, for general use.

        Parameters
        ----------
        content : string (et. al.)
            The content to print
        '''
        print(self.blue.format(content))

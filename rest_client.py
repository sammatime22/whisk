'''
This file handles the entirety of the development of the REST calls to Matcha DB.

sammatime22, 2021
'''


class RestClient():
    '''
    A REST Client for interfacing with Matcha DB. This allows the controller to ask for input args
    independently to developing, conducting, and interpreting the result of a REST request against
    the Matcha DB instance.
    '''


    # Default networking values.
    DEFAULT_PROTOCOL = "http://"   # Default is http
    DEFAULT_HOST = "127.0.0.1"     # Default is localhost
    DEFAULT_PORT = "11150"          # Default is port 8080

    # Class networking variables.
    protocol = DEFAULT_PROTOCOL
    host = DEFAULT_HOST
    port = DEFAULT_PORT


    def __init__(self, protocol = None, host = None, port = None):
        '''
        The constructor for the RestClient singleton.

        Parameters
        ----------
        protocol : string
            The protocol used to communicate to the Matcha DB instance
        host : string
            The hostname/IP used of the Matcha DB
        general_color_choice : string
            The port used of the Matcha DB
        '''
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

    
    def get_request(self):
        '''
        Runs a get request against the DB.
        '''


    def post_request(self):
        '''
        Runs a post request against the DB.
        '''


    def update_request(self):
        '''
        Runs an update (PUT) request against the DB.
        '''


    def delete_request(self):
        '''
        Runs a delete request against the DB.
        '''


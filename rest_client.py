'''
This file handles the entirety of the development of the REST calls to Matcha DB.

sammatime22, 2021
'''
import requests


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

    
    def get_protocol_host_port(self):
        '''
        Returns the protocol, host, and port used by Whisk.    

        Return
        ----------
        protocol : string
            The protocol in use by the Rest Client
        host : string
            The host in use by the Rest Client
        port : string
            The port in use by the Rest Client
        '''
        return self.protocol, self.host, self.port


    def get_request(self, from_portion, select_portion):
        '''
        Runs a get request against the DB.

        Parameters
        ----------
        from_portion : JSON Object
            The From Portion for the query to be made on MatchaDB
        select_portion : JSON Object
            The Select Portion for the query to be made on MatchaDB      

        Return
        ----------
        status : boolean
            The status of the request (successful - True, unsuccessful - False)
        response.content OR statement : string
            The content of the response or a statement containing the error
        '''
        parameter_vals = "{\"From\": " + from_portion + ", \"Select\": " + select_portion + "}"


        try:
            # Make the request and see the response code.
            response = requests.get(self.protocol + self.host + ":" + self.port + "/", data = repr(parameter_vals))
            return True, response.content
        except requests.exceptions.ConnectionError:
            return False, "A connection error has occured."
        except Exception as e:
            return False, "An unidentified error has occured: " + str(e) + "."


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


'''
Kicks off the engine for Whisk.

sammatime22, 2022
'''

from display import Display
from input_machine import InputMachine
from rest_client import RestClient
from engine import Engine
from threading import Thread

# General String Constants 
WELCOME = "Welcome to Whisk, the MatchaDB Tester!\nSammaTime22, 2021-2022"
INSUFFICIENT_ARGUMENTS = "Not enough arguments were provided to continue."


def kickstart(input_arguments):
    '''
    This method kick starts the application.
    
    Parameters:
    ----------
    input_arguments : The input arguments provided from the CLI
    '''
    # Start up the display
    whisk_display = Display()

    # Start of app
    whisk_display.print_general(WELCOME)

    # Setup for Rest Client
    host = None
    port = None
    protocol = None

    # Get the hostname, if it exists.
    if len(input_arguments) > 2:
        host = input_arguments[1]

    # Get the portname, if it exists.
    if len(input_arguments) > 3:
        port = input_arguments[2]

    if len(input_arguments) > 4:
        protocol = input_arguments[3]

    # Start up the Rest Client
    rest_client = RestClient(protocol, host, port)
    protocol, host, port = rest_client.get_protocol_host_port()

    # Start up the Input Machine
    input_machine = InputMachine()

    # Begin the Engine
    engine = Engine()
    engine_thread = Thread(target = engine.run_engine, args = (whisk_display, rest_client, input_machine))
    engine_thread.start()

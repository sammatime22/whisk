'''
The following tool helps developers and likewise check their work on MatchaDB by providing an easy
to use CLI interface, using Python 3, to run commands against the DB.

sammatime22, 2021
'''
import requests
import sys
from display import Display

# Different constants for the names of different commands used on Whisk.
GET = "GET"
POST = "POST"
UPDATE = "UPDATE"
DELETE = "DELETE"
HELP = "HELP"
EXIT = "EXIT"

# General String Constants
WELCOME = "Welcome to Whisk, the MatchaDB Tester!\nSammaTime22, 2021"

def retrieve_command(whisk_display):
    '''
    This method promts the user to provide a command, and then returns that command so that it can
    be used by the rest of the application.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    '''
    whisk_display.print_general("\nPlease provide one of the following:\nGET, POST, UPDATE, DELETE, HELP, EXIT")
    whisk_display.print_general("Do note that this is not case sensitive.")

    # Gather and return the command.
    return input("Your Command: ")


def help_command(whisk_display):
    '''
    Allows the user to get more information on different commands to better understand their 
    workings and how to use them.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    '''
    print("What command would you like more info on?\nGET, POST, UPDATE, DELETE, HELP, EXIT")
    print("This is not case sensitive.")

    # Get the selected command.
    selected_command = input("> ").upper()

    # Print help information accordingly.
    if (selected_command == GET):
        whisk_display.print_general("This command allows users to retrieve data from the DB.")
        whisk_display.print_general("Below are the promts provided with the GET command:")
        whisk_display.print_general("From: Provide the name of the table in the database you would like data from.")
        whisk_display.print_general("Select: A query of format \"key\" \"operation\" \"value\", given over three inputs.")
    elif (selected_command == POST):
        whisk_display.print_general("This command allows users to insert data into the DB.")
        whisk_display.print_general("Below are the promts provided with the POST command:")
        whisk_display.print_general("From: Provide the name of the table in the database you would like to insert data.")
        whisk_display.print_general("Select: A query of format \"key\" \"operation\" \"value\", given over three inputs.")
        whisk_display.print_general("Insert: An item to insert, in key-value pairs provided in 2D arrays in one 2D array") 
    elif (selected_command == UPDATE):
        whisk_display.print_general("This command allows users to update data in the DB.")
        whisk_display.print_general("Below are the promts provided with the UPDATE command:")
        whisk_display.print_general("From: Provide the name of the table in the database you would like to update.")
        whisk_display.print_general("Select: A query of format \"key\" \"operation\" \"value\", given over three inputs")
        whisk_display.print_general("Update: An update action of format \"key\" \"operation\" \"value\" in three inputs")        
    elif (selected_command == DELETE):
        whisk_display.print_general("This command allows users to remove data from the DB.")
        whisk_display.print_general("Below are the promts provided with the DELETE command:")
        whisk_display.print_general("From: Provide the name of the table in the database you would remove data from.")
        whisk_display.print_general("Select: A query of format \"key\" \"operation\" \"value\", given over three inputs")
    elif (selected_command == HELP):
        whisk_display.print_general("After typing help in any casing, when prompted, provide the command of interest.")
    elif (selected_command == EXIT):
        whisk_display.print_general("Just simply type exit when promted in any casing and you will exit the app.")


def get_command(whisk_display, rest_client):
    '''
    This method collects the From and Select portions for a GET request, runs it against MatchaDB,
    and prints the response code. It will also print exceptions, given that they occur.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    rest_client : RestClient
        The rest client in use by the whisk application to run the GET request on the MatchaDB
    '''
    # Gather the From portion of the command.
    from_portion = "[\"" + input("From: ") + "\"]"

    # Gather the Select portion of the command.
    spart_one = input("Select (key): ")
    spart_two = input("Select (operation): ")
    spart_three = input("Select (value): ")
    select_portion = "[[\"" + spart_one + "\", \"" + spart_two + "\", \"" + spart_three + "\"]]"

    # Use the Rest Client
    rest_client.get_command(from_portion, select_portion)


def post_command(whisk_display):
    '''
    This method collects the From, Select, and Insert portions for a POST request, runs it against
    MatchaDB, and prints the response code. It will also print exceptions, given that they occur.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    '''
    # Gather the From portion of the command.
    from_portion = "[\"" + input("From: ") + "\"]"

    # Gather the Select portion of the command.
    spart_one = input("Select (key): ")
    spart_two = input("Select (operation): ")
    spart_three = input("Select (value): ")
    select_portion = "[[\"" + spart_one + "\", \"" + spart_two + "\", \"" + spart_three + "\"]]"

    # Gather the Insert portion of the command.
    insert_portion = input("Insert: ")

    # Develop the Parameter Values.
    parameter_vals = "{\"From\": " + from_portion \
                    + ", \"Select\": " + select_portion \
                    + ", \"Insert\": " + insert_portion + "}"

    try:
        # Make the request and see the response code.
        response = requests.post(PROTOCOL + host + ":" + port + "/", data = repr(parameter_vals))
        whisk_display.print_success(response)
        whisk_display.print_success(response.content)
    except requests.exceptions.ConnectionError:
        whisk_display.print_error("A connection error has occured.")
    except Exception as e:
        whisk_display.print_error("An unidentified error has occured of type " + type(e) + ".")


def update_command(whisk_display):
    '''
    This method collects the From, Select, and Update portions for a UPDATE (put) request, runs it 
    against MatchaDB, and prints the response code. It will also print exceptions, given that they 
    occur.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    '''
    # Gather the From portion of the command.
    from_portion = "[\"" + input("From: ") + "\"]"

    # Gather the Select portion of the command.
    spart_one = input("Select (key): ")
    spart_two = input("Select (operation): ")
    spart_three = input("Select (value): ")
    select_portion = "[[\"" + spart_one + "\", \"" + spart_two + "\", \"" + spart_three + "\"]]"

    # Gather the Update portion of the command.
    upart_one = input("Update (key): ")
    upart_two = input("Update (operation): ")
    upart_three = input("Update (value): ")
    update_portion = "[[\"" + upart_one + "\", \"" + upart_two + "\", \"" + upart_three + "\"]]"

    # Develop the Parameter Values.
    parameter_vals = "{\"From\": " + from_portion \
                    + ", \"Select\": " + select_portion \
                    + ", \"Update\": " + update_portion + "}"

    try:
        # Make the request and see the response code.
        response = requests.put(PROTOCOL + host + ":" + port + "/", data = repr(parameter_vals))
        whisk_display.print_success(response)
        whisk_display.print_success(response.content)
    except requests.exceptions.ConnectionError:
        whisk_display.print_error("A connection error has occured.")
    except Exception as e:
        whisk_display.print_error("An unidentified error has occured of type " + type(e) + ".")


def delete_command(whisk_display):
    '''
    This method collects the From and Select portions for a DELETE request, runs it against 
    MatchaDB, and prints the response code. It will also print exceptions, given that they occur.

    Parameters:
    ----------
    whisk_display : Display
        The display object used by the whisk application to print content to the console
    '''   
    # Gather the From portion of the command.
    from_portion = "[\"" + input("From: ") + "\"]"

    # Gather the Select portion of the command.
    spart_one = input("Select (key): ")
    spart_two = input("Select (operation): ")
    spart_three = input("Select (value): ")
    select_portion = "[[\"" + spart_one + "\", \"" + spart_two + "\", \"" + spart_three + "\"]]"

    # Develop the Parameter Values.
    parameter_vals = "{\"From\": " + from_portion + ", \"Select\": " + select_portion + "}"

    try:
        # Make the request and see the response code.
        response = requests.delete(PROTOCOL + host + ":" + port + "/", data = repr(parameter_vals))
        whisk_display.print_success(response)
        whisk_display.print_success(response.content)
    except requests.exceptions.ConnectionError:
        whisk_display.print_error("A connection error has occured.")
    except Exception as e:
        whisk_display.print_error("An unidentified error has occured of type " + type(e) + ".")


def main():
    '''
    The main method of the application.
    '''
    whisk_display = Display()


    # Start of app
    whisk_display.print_general(WELCOME)

    protocol = None
    host = None
    port = None

    # Get the hostname, if it exists.
    if len(sys.argv) > 2:
        host = sys.argv[1]

    # Get the portname, if it exists.
    if len(sys.argv) > 3:
        port = sys.argv[2]

    rest_client = RestClient(protocol, host, port)
    protocol, host, port = rest_client.get_protocol_host_port()

    while True:
        # Remind the user where the command is currently pointed at.
        whisk_display.print_general("Using " + PROTOCOL + host + ":" + port + "/")

        # Get the command.
        command_to_use = retrieve_command(whisk_display).upper()

        # Check which command this is for and run said command accordingly.
        if (command_to_use == GET):
            get_command(whisk_display, rest_client)
        elif (command_to_use == POST):
            post_command(whisk_display, rest_client)
        elif (command_to_use == UPDATE):
            update_command(whisk_display, rest_client)
        elif (command_to_use == DELETE):
            delete_command(whisk_display, rest_client)
        elif (command_to_use == HELP):
            help_command(whisk_display)
        elif (command_to_use == EXIT):
            break


# Bootload the application.
if __name__ == "__main__":
    main()

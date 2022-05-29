'''
The following tool helps developers and likewise check their work on MatchaDB by providing an easy
to use CLI interface, using Python 3, to run commands against the DB.

sammatime22, 2021-2022
'''
import sys
sys.path.append('src')
from bootloader import kickstart

# Kickstart the application.
if __name__ == "__main__":
    kickstart(sys.argv)

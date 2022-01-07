import os

def print_art(filename):
    """Takes a filename that prints the ACSII Art 
    stored in the file"""
    art = open(filename, 'r')
    print(''.join([line for line in art]))

def clear_console():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
##
## EPITECH PROJECT, 2022
## verif_error.py
## File description:
## Function : flag_h, errors
##

import os
from sys import argv
import math
import random

def errors(c, num_arg):
    if (c == 1):
        if (num_arg == 1):
            flag_h(1)
        elif (num_arg == 2):
            flag_h(2)
            return (0)
    return (84)

def flag_h(c):
    if (c == 1):
        print("USAGE : ./103cipher [message] [key] [flag]")
    else:
        print("USAGE\n    ./103cipher message key flag\n")
        print("DESCRIPTION")
        print("    message\ta message, made of ASCII characters")
        print("    key\t\tthe encryption key, made of ASCII characters")
        print("    flag\t0 for the message to be encrypted, 1 to be decrypted")

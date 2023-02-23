#!/usr/bin/python3

##
## EPITECH PROJECT, 2022
## 103cipher
## File description:
## Function : main
##

import os
import math
from sys import argv
from src.verif_error import errors
from src.encrypt import encrypt
from src.decrypt import decrypt

def main(ac, av):
    if (ac == 1 or (ac == 2 and av[1] == "-h")):
        exit(errors(1, ac))
    elif (ac != 4):
        exit(errors(2, ac))
    if (av[3] not in ["0", "1"]):
        exit(84)
    encrypt(ac, av) if (av[3] == "0") else decrypt(ac, av)

main(len(argv), argv)
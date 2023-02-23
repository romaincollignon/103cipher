##
## EPITECH PROJECT, 2022
## encrypt.py
## File description:
## Function : msg_matrix, encrypt
##

import os
import math
from src.verif_error import errors
from src.function import print_key, print_encrypt
from src.matrix import key_matrix, mess_matrix

def msg_matrix(key, message):
    result = [[0] * len(message[0]) for i in range(len(message))]
    for i in range(len(message)):
        for j in range(len(message[0])):
            for k in range(len(message[0])):
                result[i][j] += (key[k][j] * message[i][k])
    return result

def encrypt(ac, av):
    key = key_matrix(av[2])
    msg = mess_matrix(av[1], len(key))
    result = msg_matrix(key, msg)
    print_key(key)
    print()
    print_encrypt(result)

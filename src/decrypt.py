##
## EPITECH PROJECT, 2022
## decrypt.py
## File description:
## Function : decrypt_calc_2, decrypt_calc_3, decrypt_2, decrypt_3
##

import os
import math
from src.verif_error import errors
from src.function import print_key, print_decrypt
from src.matrix import key_matrix, decrypt_matrix
from src.encrypt import msg_matrix

def decrypt_calc_2(key):
    return key[0][0] * key[1][1] - key[0][1] * key[1][0]

def decrypt_calc_3(key):
    return (key[0][0] * ((key[1][1] * key[2][2]) - (key[1][2] *key[2][1]))
    - key[0][1] * ((key[1][0] * key[2][2]) - (key[1][2] * key[2][0]))
    + key[0][2] * ((key[1][0] * key[2][1]) - (key[1][1] * key[2][0])))

def decrypt_2(key):
    tmp = decrypt_calc_2(key)
    if (tmp == 0):
        exit(84)
    return [[key[1][1] / tmp, -key[0][1] / tmp],
            [-key[1][0] / tmp, key[0][0] / tmp]]

def decrypt_3(key):
    matrix = [[0] * 3 for k in range(3)]
    tmp = decrypt_calc_3(key)
    if (tmp == 0):
        exit(84)
    for i in range(3):
        for j in range(3):
            calc = [[n for k, n in enumerate(row) if (k != i)]
                        for m, row in enumerate(key) if (m != j)]
            a = decrypt_calc_2(calc)
            sign = math.pow(-1, i + j)
            matrix[i][j] = sign * a / tmp
            if (matrix[i][j] == -0.0):
                matrix[i][j] = 0.0
    return matrix

def decrypt(ac, av):
    key = key_matrix(av[2])
    if (len(key) == 1):
        key[0][0] = 1 / key[0][0]
    elif (len(key) == 2):
        key = decrypt_2(key)
    elif (len(key) == 3):
        key = decrypt_3(key)
    else:
        exit(errors(4, 4))
    msg = decrypt_matrix(av[1], len(key))
    print_key(key)
    result = msg_matrix(key, msg)
    print()
    print_decrypt(result)

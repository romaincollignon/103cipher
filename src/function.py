##
## EPITECH PROJECT, 2022
## function.py
## File description:
## Function : print_key, print_encrypt, print_decrypt
##

import math
import os

def print_key(matrix):
    print("Key matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print(round(matrix[i][j], 3), end = '\t')
            else:
                print(round(matrix[i][j], 3), end = '')
        print()

def print_decrypt(matrix):
    print("Decrypted message:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            c = chr(round(matrix[i][j]))
            if (c.isprintable()):
                print(c, end = '')
        if (i == len(matrix) - 1):
            print()

def print_encrypt(matrix):
    print("Encrypted message:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print(matrix[i][j], end = ' ')
            else:
                print(matrix[i][j], end = '')
        if (i < len(matrix) - 1):
            print(end = ' ')
        else:
            print()

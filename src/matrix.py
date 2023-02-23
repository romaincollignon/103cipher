##
## EPITECH PROJECT, 2022
## matrix.py
## File description:
## Function : key_matrix, mess_matrix, decrypt_matrix
##

import os
import math

def mess_matrix(str, n):
    size = math.ceil(len(str) / n)
    matrix = [[0] * int(n) for i in range(int(size))]

    i, j = 0, 0
    for pos in range(len(str)):
        matrix[i][j] = ord(str[pos])
        i = (i + 1) if (j == (n - 1)) else i
        j = 0 if (j == (n - 1)) else (j + 1)
    return matrix

def key_matrix(str):
    size = math.ceil(math.sqrt(len(str)))
    matrix = [[0] * int(size) for i in range(int(size))]

    i, j = 0, 0
    for pos in range(len(str)):
        matrix[i][j] = ord(str[pos])
        i = (i + 1) if (j == (size - 1)) else i
        j = 0 if (j == (size - 1)) else (j + 1)
    return matrix

def decrypt_matrix(str, n):
    tab = [int(i) for i in str.split() if i.isdigit()]
    size = len(tab) / n
    matrix = [[0] * int(n) for i in range(int(size))]
    i, j = 0, 0
    for pos in range(len(tab)):
        matrix[i][j] = tab[pos]
        i = (i + 1) if (j == (n - 1)) else i
        j = 0 if (j == (n - 1)) else (j + 1)
    return matrix
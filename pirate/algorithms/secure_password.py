#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'getStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING password
#  2. INTEGER weight_a
#

def getStrength(password, weight_a):
    letters = string.ascii_lowercase
    strength = 0
    for p in password:
        score = (letters.find(p) + weight_a) % 26
        print(p)
        print(score)
        strength += score

    return strength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = input()

    weight_a = int(input().strip())

    strength = getStrength(password, weight_a)

    fptr.write(str(strength) + '\n')

    fptr.close()

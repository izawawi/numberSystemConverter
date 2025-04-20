from forceInt import ForceInt
import numpy as np
from numpy.ma.core import remainder
remainder = 0
decimal = 1
#decimal_to_binary_list = []
#reversed_darr = []

def decimal_to_binary():
    decimal = input("Enter a decimal number: ")
    unum = decimal
    decimal = ForceInt(decimal)
    remainder = decimal
    decimal_to_binary_list = []
    reversed_darr = []

    while decimal != 0:
        remainder = decimal
        decimal = decimal // 2
        decimal = ForceInt(decimal)

        # remainder = decimal
        remainder = remainder % 2

        if remainder != 0:
            remainder = 1
        elif remainder == 0:
            remainder = 0


        decimal_to_binary_list.append(remainder)



    while len(decimal_to_binary_list) % 4 > 0:
        decimal_to_binary_list.append(0)



    #print(reversed_darr)
    reversed_darr = decimal_to_binary_list[::-1]
    b = list(map(str, reversed_darr))
    total =''.join(b)
    print("Decimal (" + unum + ")₁₀ is equal to (" + total + ")₂")
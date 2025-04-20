import numpy as np
from forceInt import ForceInt
from decimalToBinary import decimal_to_binary
from binaryToDecimal import binary_to_decimal



while True:
    print("Enter Your Choice")
    menuOption = input("1: Binary to Decimal Converter\n2: Decimal to Binary Converter\n3: Exit\n")

    if menuOption == "1":
        binary_to_decimal()

    elif menuOption == "2":
        decimal_to_binary()
    elif menuOption == "3":
        break





import numpy as np

def binary_to_decimal():
    total = 0
    loop = 0
    binarynum = input("Enter a binary number: ")
    arr = np.array([int(char) for char in binarynum])


    reversed_arr = arr[::-1]
    length_of_array = len(reversed_arr)


    while loop < length_of_array:
        array_value = reversed_arr[loop]
        new_element = array_value * (2 ** loop)
        loop = loop + 1

        total += new_element



    print(" ")
    print("Binary (" + binarynum + ")₂ is equal to (" + str(total)+")₁₀")





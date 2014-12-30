def flip_bit(number, n):
    msk = (0b1 << (n-1))
    result = number ^ msk
    return bin(result)
"""
Define a function called flip_bit that takes the inputs (number, n).
Flip the nth bit (with the ones bit being the first bit) and store it in result.
Return the result of calling bin(result).

"""
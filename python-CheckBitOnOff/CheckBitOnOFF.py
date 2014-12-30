
def check_bit4(input):
    num = 0b1000
    if input & num:
        return "on"
    else:
        return "off"
    
"""
Define a function, check_bit4, with one argument, input, an integer.
It should check to see if the fourth bit from the right is on.
If the bit is on, return "on" (not print!)
If the bit is off, return "off".
"""
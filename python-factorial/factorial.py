def factorial(x):
    if x == 0:
        return x
    elif x == 1:
        return 1
    else:
        i = 1
        fact = 1
        temp = x
        for i in range( x ):
            fact *= temp
            temp -= 1
        return fact
            
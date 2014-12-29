def digit_sum(n):
    s = 0;
    while( n > 0):
        temp = n % 10
        s += temp
        n /= 10
    return s
    
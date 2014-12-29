def is_int(x):
    if type(x) == type(1) or x - int(x) == 0:
        return True
    else:
        return False
# cython: language_level=3

def core_method(num):
    if num > 0:
        return core_method(num - 1)
    else:
        return 1

# writw a pyhton program to calcute the geometic sum of n-1.


def geometric_sum(n):
    if n<0:
        return 0
    else:
        return 1/(pow(2,n)) + geometric_sum(n-1)
print(geometric_sum(7))
print(geometric_sum(4))


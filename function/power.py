# writw a pyhton program to calcute the value of 'a' to the power.


def power(a,b):
    if b==0:
        return 1
    elif a==0:
        return 0
    elif b==0:
        return a
    else:
        return a*power(a,b-1)
print(power(3,4))
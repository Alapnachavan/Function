# write a pyhton program to find the gretest commo.


def Recurgcd(a,b):
    low=min(a,b)
    high=max(a,b)

    
    if low==0:
        return high
    elif low==1:
        return 
    else:
        return Recurgcd(low,high%low)
print(Recurgcd(10,12))
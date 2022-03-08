# write a python program to the sum of a non-negative interger.
# test Data 
# sumDigits (345) -> 12
# sumDigit(45)
# -> 9
    


def sumDigits(n):
    if n==0:
      return 0
    else:
        return n%10+sumDigits(int(n/10))
print(sumDigits(345))
print(sumDigits(45))

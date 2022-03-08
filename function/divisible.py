# def divisible(a):
#     i=1
#     while i<=a:
#         if a%i==0:
#             print(i)
#         i=i+1
# divisible(10)


def myfunc(n):
  return lambda a : a * n
 
mytripler = myfunc(3)

print(mytripler(11))

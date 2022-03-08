def number(n):
    num=0
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if num==rev:
        print(num,"numberis palindrom")
    else:
        print(num,"number is not palindrom ")
number(707)
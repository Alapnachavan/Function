def letter():
    num=input("enter the your letter or digit:")
    if num>="A" and num<="Z":
        print(num,"its a uppercase letter")
    elif num>="a" and num<="z":
        print(num,"its a lower case letter")
    elif num>="0" and num<="9":
        print(num,"is a digit")
    else:
        print(num,"its a special charector")
letter()
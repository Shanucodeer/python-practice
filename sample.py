a=int(input("Enter your first digit: "))
b=int(input("Enter your second digit: "))
c=str(input("Enter arthimatic +,-,*,/: "))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else :
    print("Enter valid input")
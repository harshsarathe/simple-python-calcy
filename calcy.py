operation=input(print("+","-","*","/","slect one operation"))
a=float(input("value of a"))
b=float(input("value of b"))

if(operation=="+"):

    print(a,operation,b"=",a+b)
elif(operation=="-"):
    print(a,operation,b"=",a-b)
elif(operation=="*"):

     print(a,operation,b"=",a*b)
elif(operation=="/"):

     print(a,operation,b"=",a/b)
else:
     print("invalid")
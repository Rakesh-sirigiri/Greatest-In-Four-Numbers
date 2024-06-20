a = int(input("enter first:"))
b = int(input("enter second:"))
c = int(input("enter third:"))
d = int(input("enter fourth:"))
if(a>b and a>c and a>d):
    print("greatest is:",a)
elif(b>c and b>d):
    print("greatest is:",b)
elif(c>d):
    print("greatest is:",c)
elif(d>c):
    print("greatest is:",d)
else:
    print("enter any two values are equal or four values equal")

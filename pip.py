num = int(input("enter the nummber :" ))
a = 0
b = 1
print(a)
print(b)
for i in range(0,num):
    c = a+b
    a = b
    b = c
    print(c)
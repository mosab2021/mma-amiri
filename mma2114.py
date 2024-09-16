a = 10
if  a == 10:
    print(True)
else:
    print(False)

a = 11
print(True) if a == 10 else print(False)

x = [i for i in range(10)]
print(x)

x = [i**2 for i in range(10)]
print(x)




x = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(10)]
print(x)

name = "Mohammad Mahdi Amiri"

x = [c for c in name] 
print(x)

x = [c if c != "a" else 0 for c in name] 
print(x)

x = [c.upper() for c in name] 
print(x)

x = [i for i in range(10) if i % 2 == 0]
print(x)


x = input("please enter a number:")
print(x)

a,b,c = input("please enter some numbers : ").split(",",3)
print(a,b,c)


x = input("please enter some numbers : ").split(" ")
print(x)


x = input("please enter some numbers : ").split()
print(x)

x = [i for i in input("please enter some numbers : ").split()]
print(x)

x = [int(i) for i in input("please enter some numbers : ").split()]
print(x)

x = [int(i) ** 3 if int(i) % 2 == 0 else int(i) ** 2  for i in input("please enter some numbers : ").split()]
print(x)


x = [10, 12, False, "ali", "reza" , False, 16.5, 3 > 8 , 12.5 < 18 , 33]
print(x)

a = list(filter(lambda i:i,x))
print(a)

def myFunc(i):
    if i % 2 == 0:
        return True
    else:
        return False


def myFunc(i):
    if i % 2 == 0:
        return i
    else:
        return False


l1 = [10,11,13,14,15,16,12,17,19]
x = list(filter(myFunc, l1))
print(x)


l1 = [10,11,13,14,15,16,12,17,19]
x = list(map(myFunc, l1))
print(x)


x = [i for i in input("please enter some numbers : ").split()]
print(x)

x = list(map(int,[i for i in input("please enter some numbers : ").split()]))
print(x)


x = list(filter(lambda i: i % 2 ==0, list(map(int,[i for i in input("please enter some numbers : ").split()]))))
print(x)












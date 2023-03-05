a = int(input("enter first number: "))
b = int(input("enter second number: "))
def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a-1,b+1)
print(f"{a} + {b} = {sum(a,b)}")
a = int(input("enter number: "))
b = int(input("enter degree: "))
def degree(a,b):
    if b == 0:
        return 1
    else:
        return a * degree(a, b-1)


print(f"result = {degree(a ,b )}")
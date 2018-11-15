# a = int(input("nhap a: "))
# b = int(input("nhap b: "))
# print("tong 2 so:", a + b)

# a = int(input("nhap a: "))
# ope = input("operation +, -, *, / :")
# b = int(input("nhap b: "))
def eval(a, b, op):
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a*b
    elif op == "/":
        r = a/b
    else:
        print("none")
    return r
# s = eval(4, 5, "-")
# print(s)


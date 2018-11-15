from random import randint
from random import randint, choice
from calc_intro import eval
def generate_quiz():
    x = randint(0, 10)
    op_list = [ "+", "-", "*", "/"]
    o = choice(op_list)

    y = randint(0, 10)
    c = randint(-2, 2)
    r = eval(x, y, o) + c
    return x, y, o, r, c
a, b, o, r, c= generate_quiz()

#print(a, o, b, "=", r)
#x = input("nhập Y/N: ")

#if c == 0:
    #if x.upper() == "Y":
        #print("bạn đúng")
    #else:
        #print("sai oyyyy!!!")
#else:
    #if x.upper() == "N":
        #print("bạn đúng")
    #else:
        #print("sai oyyyy!!!")
   

    


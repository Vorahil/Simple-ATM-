

money=0

def check():
    print("{0:-^60}".format("You money is{}".format(money)))

def depoist():
    num=eval(input("Please input the money you depoist"))
    global money
    money+=num
    print("{0:-^60}".format("You money is{}".format(money)))

def withdraw():
    while True:
        num=eval(input("Please input the money you withdraw"))
        global money
        number=money
        number -= num
        if number<0:
            print("You don't have enough money")
            continue
        else:
            money -= num
            print("{0:-^60}".format("You money is{}".format(money)))
            break
def main():
    print("{0:-^60}".format("Welcome to Simple ATM"))
    print("\tChoose your purpose")
    print("""\tIf you want to check,please input 1
    \tIf you want to depoist,please input 2
     \tIf you want to withdraw,please input 3
     \tIf you want to exit,please input 4""")
    while True:
        choice=eval(input("Please input your answer"))
        if choice==1:
            check()
            continue
        elif choice==2:
            depoist()
            continue
        elif choice==3:
            withdraw()
            continue
        elif choice==4:
            print("Welcom you use next time")
            break
        else:
            print("Input the correct option")
            continue

main()




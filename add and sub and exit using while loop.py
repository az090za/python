def menu():
    print("1) Add two number ")
    print("2) Subtrat two number ")
    print("3) exit ")

#---------------------------------------------
menu()
N=int(input("Enter Numbers: "))
while N!=0:
    if N ==1:
        a1=int(input("Enter First Number: "))
        b2=int(input("Enter Second Number: "))
        print(a1+b2)
    elif N ==2:
        a1=int(input("Enter First Number: "))
        b2=int(input("Enter Second Number: "))
        print(a1-b2)      
        
    menu()
    N=int(input("Enter Numbers: "))
            
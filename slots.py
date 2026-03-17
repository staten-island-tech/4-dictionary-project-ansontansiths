""" balance = int(input("Enter the amount of money you want to start with? "))
if balance < 1 or balance > 1000:
    print("Invalid Amount")

FirstP = int(input("Last win on first machine?"))
SecondP = int(input("Last win on second machine?"))
ThirdP = int(input("Last win on third machine?"))
Times = 0 
First = FirstP
Second = SecondP
Third = ThirdP """
"""def slots(balance, First, Second, Third):
    times=0
    while balance>= 1 and balance < 1000:
        First += 1
        balance -= 1
        times+=1
        if First >= 1 and First >=35:
         First = 0
         balance -= 1
         times+=1
        elif Second >= 1 and Second >=100:
            Second = 0
            balance -= 1
            times+=1
        elif Third >= 1 and Third >=10:
            Third = 0
            balance -= 1
            times+=1
        elif First == 35:
         balance += 30
         First = 0
        elif Second == 100:
         balance += 60
         Second = 0
        elif Third == 10:
         balance += 9
         Third = 0
        elif balance == 0:
         First = 0
         Second = 0
         Third = 0
         print("you played",times,"times before going broke lmfao")
slots(48,3,10,4)"""
def slots(balance, First, Second, Third):
    times=0
    while balance>= 1 and balance < 1000:
        First += 1
        balance -= 1
        times+=1
        if First >= 1 and First >=35:
         First = 0
         balance -= 1
         times+=1
        elif Second >= 1 and Second >=100:
            Second = 0
            balance -= 1
            times+=1
        elif Third >= 1 and Third >=10:
            Third = 0
            balance -= 1
            times+=1
        elif First == 35:
         balance += 30
         First = 0
        elif Second == 100:
         balance += 60
         Second = 0
        elif Third == 10:
         balance += 9
         Third = 0
        elif balance == 0:
         First = 0
         Second = 0
         Third = 0
         print("you played",times,"times before going broke lmfao")
slots()
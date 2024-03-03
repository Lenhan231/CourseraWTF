import random

def botwin(YC,BC):
    global YS, BS
    YS -= YC
    BS += YC
    print("Bot chose", BC)
    print("Bot Win")
    print("Your coin at present:", YS)
    print("Bot coin at present: ", BS)

def botlose(BC):
    global YS, BS
    YS += BC
    BS -= BC
    print("Bot chose", BC)
    print("Bot lose")
    print("Your coin at present:", YS)
    print("Bot coin at present: ", BS)

def chan():
    global YS, BS
    YC = int(input("Input your coin: "))
    while YS != 0:
        if BS == 2:
           BC = 1 if YC % 2 != 0 else 2  
           botwin(YC, BC)
        else:
            BC = random.randint(1, BS - 2)
            if (YC + BC) % 2 == 0:
                botlose(YC)
            else:
                botwin(YC, BC)
        if YS != 0 :
            YC = int(input("Input your coin: "))
            while YC > YS:
                YC = int(input("Please reinput your coin it is invalid because your coin is smaller than your input coin: "))
    print("You lose")

def le():
    global YS, BS
    YC = int(input("Input your coin: "))
    while YS != 0:
        if BS == 2:
           BC = 2 if YC % 2 != 0 else 1  
           botwin(YC, BC)
        else:
            BC = random.randint(1, BS - 2)
            while int(BC) == YC:
                BC = random.randint(1, BS - 2)
            if (YC + int(BC)) % 2 != 0:
                botlose(YC)
            else:
                botwin(YC, BC)
        if YS != 0 :
            YC = int(input("Input your coin: "))
            while YC > YS:
                YC = int(input("Please reinput your coin it is invalid because your coin is smaller than your input coin: "))
    print("You lose")
    
       
def main():
    print("Both Bot and Player start with 10 coin")
    role = int(input("Press 1 to chose EVEN and 2 to chose ODD: "))
    global YS, BS
    YS = int(20)  # Số đồng xu của bạn
    BS = int(20)  # Số đồng xu của máy
    print("Your coin at present:", YS)
    print("Bot coin at present: ", BS)
    if role == 1:
        print("You Chose Even")
        chan()
    else:
        print("You Chose Odd")
        le()

main()
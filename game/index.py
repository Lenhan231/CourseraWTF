import random

def botwin(YC, BC):
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
        else:
            BC = random.randint(1, min(2, BS))  # Adjusted to ensure BC doesn't exceed BS
            
        if (YC + BC) % 2 == 0:
            botlose(YC)
        else:
            botwin(YC, BC)
        
        if YS != 0:
            YC = int(input("Input your coin: "))
            while YC > YS:
                YC = int(input("Please reinput your coin it is invalid because your coin is smaller than your input coin: "))
        if BS <= 0:
            print("Bot lose the game")
            exit()
    print("You lose the game")

def le():
    global YS, BS
    YC = int(input("Input your coin: "))
    while YS != 0:
        if BS == 2:
            BC = 2 if YC % 2 != 0 else 1
        else:
            BC = random.randint(1, min(2, BS))  # Adjusted to ensure BC doesn't exceed BS - 1
            
        if (YC + BC) % 2 != 0:
            botlose(YC)
        else:
            botwin(YC, BC)
        
        if YS != 0:
            YC = int(input("Input your coin: "))
            while YC > YS:
                YC = int(input("Please reinput your coin it is invalid because your coin is smaller than your input coin: "))
        if BS <= 0:
            print("Bot lose the game")
            exit()
    print("You lose the game")

def main():
    print("Both Bot and Player start with 10 coin")
    role = int(input("Press 1 to choose EVEN and 2 to choose ODD: "))
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

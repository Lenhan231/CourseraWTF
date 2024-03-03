import random
BS = 7
BC = random.randint(1, BS - 2)
YC = int(input())

print("a",BC)

while int(BC) == YC:
    BC = random.randint(1, BS - 2)
    print("b",BC)

print("c",BC)
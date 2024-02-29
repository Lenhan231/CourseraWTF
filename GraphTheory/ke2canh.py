with open("dske.txt","r") as f:
    m = int(f.readline())
    a = [[1 for i in range(m)] for i in range(m)]
    for i in range(m):
        a[i] = list(map(int,f.readline().split()))
    for i in range(m):
        for j in range(len(a[i])):
            if i<a[i][j]:
                print(f"{i+1} {a[i][j]}")
    
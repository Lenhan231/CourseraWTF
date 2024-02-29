with open("dsmatran.txt","r") as f:
    m = int(f.readline())
    a = [[0] for i in range(m)]
    for i in range(m):
        a[i] = list(map(int,f.readline().split()))
    
    for i in range(m):
        for j in range(m):
            if a[i][j] == 1 and i<j:
                print(f"{i+1} {j+1}")
           
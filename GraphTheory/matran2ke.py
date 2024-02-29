with open("dsmatran.txt", "r") as f:
    m = int(f.readline())
    a = [[0] for _ in range(m+1)]  # Initialize a 2D array with zeros
    adj = [[] for _ in range(m+1)]
    # Populate the 2D array based on file input
    for i in range(1, m+1):
        a[i] = list(map(int, f.readline().split()))

    # Print pairs where a[i][j] == 1
    for i in range(1, m+1):
        for j in range(0, m):
            if a[i][j] == 1:
                adj[i].append(j+1)

    for i in range(1, m + 1):
          print(f"{i}: {sorted(adj[i])}")
with open("dske.txt", "r") as f:
    m = int(f.readline())
    a = [[] for _ in range(m)]

    max_value = 0  # To store the maximum value in the input

    for i in range(m):
        a[i] = list(map(int, f.readline().split()))
        max_value = max(max_value, max(a[i]))

    # Initialize a 2D array with zeros, considering the maximum value in a
    b = [[0 for _ in range(max_value + 1)] for _ in range(m)]

    for i in range(1, m):
        for value in a[i]:
            b[i][value] = 1

    for row in b:
        print(*row)
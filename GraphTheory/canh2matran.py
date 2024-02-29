try:
    with open("dscanh.txt", "r") as f:
        # Read the first line for n and m
        n, m = map(int, f.readline().split())

        # Initialize the 2D array with zeros
        a = [[0 for _ in range(n)] for _ in range(n)]

        # Read the remaining lines for edges and update the 2D array
        for _ in range(m):
            line = f.readline().strip()
            if not line:
                continue  # Skip empty lines

            x, y = map(int, line.split())
            a[x-1][y-1] = a[y-1][x-1] = 1

        # Print the 2D array
        for row in a:
            print(*row)

except FileNotFoundError:
    print("The file 'ltdt1.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

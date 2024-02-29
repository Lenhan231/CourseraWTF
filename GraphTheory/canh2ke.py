with open("dscanh.txt", "r") as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(1001)]
    dem = []
    visit=[False]*(m+1)
    for i in range(m):
        x,y = list(map(int,f.readline().split()))
        adj[x].append(y)
        adj[y].append(x)
    def bfs(visit,dem,adj,u):
        if visit[u] == False:
            visit[u] == True
            dem.append(u) 


bfs(visit,dem,adj,1)
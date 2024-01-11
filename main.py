import sys


sys.stdin = open('graph.inp', 'r')
sys.stdout = open('graph.out', 'w')

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dd = [2, 3, 0, 1]

n, m, k =  map(int,(input().split()))
vis = []  
trace = []
for i in range(n):
    tmp = [0] * m
    vis.append(tmp)
    tmp = [-1] * m
    trace.append(tmp)


for i in range(k):
    u, v = map(int, (input().split()))
    vis[u][v] = 1
    
sx, sy, ex, ey = map(int, (input().split()))

Q = []
Q.append((sx, sy))
vis[sx][sy] = 1
l, r = 0, 0
while l <= r:
    u, v = Q[l][0], Q[l][1]
    l+= 1
    if u == ex and v == ey:
        break
    for i in range(4):
        x = u + dx[i]
        y = v + dy[i]
    
        if x < 0 or x >= n or y < 0 or y >= m:
            continue 
        if vis[x][y]:
            continue
        
        vis[x][y] = True
        trace[x][y] = dd[i]
        Q.append((x, y))
        r+= 1
    
res = []
x, y = ex, ey
res.append((x, y)) 
while x != sx or y != sy:
    dir = trace[x][y]
    xx = x + dx[dir]
    yy = y + dy[dir]
    res.append((xx, yy))
    x, y = xx, yy
print(len(res))
for i in range(len(res) - 1, -1, -1):
    print(res[i][0], res[i][1])
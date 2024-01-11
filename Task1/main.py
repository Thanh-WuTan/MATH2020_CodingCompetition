import sys
import numpy as np
import os

listInp = []
for dirname, _, filenames in os.walk('./sample/'):
    for filename in filenames:
        if filename[-3:]  == 'inp':
            listInp.append(os.path.join(dirname, filename))
listInp = sorted(listInp)

for idx, filename in enumerate(listInp):
    '''
    this is read file template
    '''
    input_file = filename
    counter = filename.split('.')[1].split('/')[-1]
    counter = int(counter[6:])


    

    sys.stdin = open(filename, 'r')

    dx = np.array([0, -1, 0, 1])
    dy = np.array([-1, 0, 1, 0])
    dd = np.array([2, 3, 0, 1])

    n, m, k =  map(int,(input().split()))
    vis = np.zeros((n, m),  dtype=int)
    trace = np.zeros((n, m),  dtype=int)


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

    '''
    this is template of writing result
    '''
    path = []
    if not os.path.exists('./result'):
        os.mkdir('./result')
    sourceFile = open(f'./result/sample{counter}.out', 'w')
    print(len(res), file = sourceFile)
    for i in res[::-1]:
        print(*i, file = sourceFile)
    sourceFile.close()
import sys 
import heapq as hq
import os 

def create_array(value, n, m):
    res = []
    for i in range(n):
        tmp = [value] * m
        res.append(tmp)
    return res

def calculatehHvalue(x, y, ex, ey, v):
    return (abs(ex - x) + abs(ey - y)) * v

def main():    
    n, m, l =  map(int,(input().split()))

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    dd = [2, 3, 0, 1]

    weight = create_array(-1, n, m)
    trace = create_array(-1, n, m)
    g = create_array(int(1e9), n, m)
    f = create_array(int(1e9), n, m)

    for i in range(l):
        u, v = map(int, (input().split())) 
        weight[u][v] = -2 # (u, v) is blocked

    sx, sy, ex, ey = map(int, (input().split()))
    f[sx][sy] = 0
    g[sx][sy] = 0
    
    h = int(input())
    avg = 0
    for i in range(h):
        u, v, w = map(int, (input().split()))
        weight[u][v] = w 
        avg+= w

    j, k = map(int, (input().split()))
    avg+= (n * m - h - l) * j
    avg//= (n * m)

    # A* search
    open_list = [(0, (sx, sy))] 
    isclosed = create_array(False, n, m)
    
    found = False
    while open_list:
        current_f, current_cell = hq.heappop(open_list)
        u, v = current_cell[0], current_cell[1]
        isclosed[u][v] = True
        for i in range(4):
            x = u + dx[i]
            y = v + dy[i]
            if x < 0 or x >= n or y < 0 or y >= m: # Out of the boundary
                continue 
            if weight[x][y] == -2: # is blocked
                continue
            if isclosed[x][y] == True:
                continue
            w = weight[x][y]
            if w == -1:
                w = j
            w = 1 + k * w
            newg = current_f + w
            newh = calculatehHvalue(x, y, ex, ey, avg)
            newf = newg + newh

            if x == ex and y == ey:
                trace[x][y] = dd[i] 
                f[x][y] = newf
                g[x][y] = newg
                found = True
                break
            
            if f[x][y] == int(1e9) or f[x][y] > newf:
                hq.heappush(open_list, (newf, (x, y)))
                trace[x][y] = dd[i]
                f[x][y] = newf
                g[x][y] = newg

        if found == True:
            break 
    # Trace the path
    assert(found == True)
    path = [] 
    u, v = ex, ey
    path.append((u, v))
    while True:
        dir = trace[u][v]
        x = u + dx[dir]
        y = v + dy[dir]
        u, v = x , y
        path.append((u, v))
        if (u == sx and v == sy):
            break


    # Output

    print(len(path)) 
    for cell in path[::-1]:
        print(cell[0], cell[1])


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

    sys.stdin = open(input_file, 'r')

    if not os.path.exists('./result'):
        os.mkdir('./result')
    sys.stdout = open(f'./result/sample{counter}.out', 'w') 
    main()

import sys
import numpy as np
import heapq as hq


sys.stdin = open('sample_task2.inp', 'r')
sys.stdout = open('sample_task2.out', 'w')

def main():    
    n, m, k =  map(int,(input().split()))

    dx = np.array([0, -1, 0, 1])
    dy = np.array([-1, 0, 1, 0])
    dd = np.array([2, 3, 0, 1]) 

    distance = np.full((n, m), int(1e9), dtype=int) 
    weight = np.full((n, m), -1, dtype=int)
    trace = np.zeros((n, m),  dtype=int)

    for i in range(k):
        u, v = map(int, (input().split())) 
        weight[u][v] = -2 # (u, v) is blocked

    sx, sy, ex, ey = map(int, (input().split()))
    distance[sx][sy] = 0
    h = int(input())
    for i in range(h):
        u, v, w = map(int, (input().split()))
        weight[u][v] = w 
    j, k = map(int, (input().split()))
    current_cell = (1, 2) 
    # dijkstra
    heap = [(0, (sx, sy))]
    
    while heap:
        current_distance, current_cell = hq.heappop(heap)
        
     
        if current_cell == (ex, ey):
            break
        u, v = current_cell[0], current_cell[1]

        if distance[u][v] < current_distance:
            continue
        for i in range(4):
            x = u + dx[i]
            y = v + dy[i]
            if x < 0 or x >= n or y < 0 or y >= m: # Out of the boundary
                continue 
            if weight[x][y] == -2: # is blocked
                continue
            w = weight[x][y]
            if w == -1: # initial, all cells have weight -1, and as default which will have weight j  
                w = j
            w = k * w + 1 # change the weight to k * w + 1
            if current_distance + w < distance[x][y]:
                distance[x][y] = current_distance + w
                trace[x][y] = dd[i]
                hq.heappush(heap, (current_distance + w, (x, y)))
            
    # Trace the path
    path = []
    u, v = ex, ey
    path.append((u, v))
    cnt = 0
    while True:
        cnt+= 1
        if cnt == 21:
            break
        dir = trace[x][y]
        x = u + dx[dir]
        y = v + dy[dir]
        u, v = x , y
        path.append((u, v))
        if (u == sx and v == sy):
            break

    # Output
    print(distance[ex][ey])
    for cell in path[::-1]:
        print(cell[0], cell[1])
main()
# Task 2 Method Explaination
### Task Summary:
In Task 2, the goal is to find the optimal path in a complex graph where each cell in the grid has associated weights. The challenge is to navigate from a starting point (sx, sy) to an ending point (ex, ey) while considering the least number of steps and the least power consumption. The grid may contain blocked cells, and the weights for each cell are dynamic. The task involves implementing Dijkstra's algorithm to find the optimal path and then tracing this path.

### Approach:
Let's go through the code step by step, explaining each part in detail:

### 1. Input Reading:

```python
n, m, k =  map(int,(input().split()))

dx = np.array([0, -1, 0, 1])
dy = np.array([-1, 0, 1, 0])
dd = np.array([2, 3, 0, 1]) 

distance = np.full((n, m), int(1e9), dtype=int) 
weight = np.full((n, m), -1, dtype=int)
trace = np.zeros((n, m), dtype=int)

for i in range(k):
    u, v = map(int, input().split()) 
    weight[u][v] = -2  # (u, v) is blocked
    
sx, sy, ex, ey = map(int, input().split())
distance[sx][sy] = 0

h = int(input())
for i in range(h):
    u, v, w = map(int, input().split())
    weight[u][v] = w 

j, k = map(int, input().split())
```

- Reads the dimensions of the grid (`n` rows and `m` columns) and the number of blocked cells (`k`).

- `dx` and `dy` represent the possible movements in the x and y directions.
- `dd` represents the corresponding directions in terms of indices (0: left, 1: up, 2: right, 3: down).

- `distance`: Represents the minimum distance to reach each cell. Initialized to a large value (`int(1e9)`) initially.
- `weight`: Represents the weights of each cell. Initialized to -1, indicating unweighted cells.
- `trace`: Used to trace the path back from the destination to the source.

- Reads the coordinates of blocked cells and marks them with a weight of -2.
- Reads the coordinates of the source (`sx`, `sy`) and destination (`ex`, `ey`) cells.

- Initializes the distance to the source as 0.

- Reads additional weights for specific cells (`u`, `v`) with values `w`.

- Reads the values of `j` and `k`.
### 2. Dijkstra's Algorithm:

  ```python
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
  ```

1. **Problem**: The code is designed to solve the problem of finding the shortest path in a grid from a source cell `(sx, sy)` to a destination cell `(ex, ey)`. The grid can have blocked cells and cells with different weights. The cost of a path is defined as `s + k * c`, where `s` is the number of steps, `k` is a constant, and `c` is the sum of the weights of the cells in the path.

2. **Approach**: The code uses Dijkstra's algorithm to find the shortest path. Dijkstra's algorithm is a greedy algorithm that finds the path with the minimum distance from the source to the destination. However, the cost `s + k * c` cannot be used directly in Dijkstra's algorithm, because it is not consistent with the principle of optimality. That is, the optimal path may not be composed of optimal subpaths.

3. **Transformation**: Assume that the optimaized road includes the s cells with the coordinate form as below:
```
        sx, sy
        x2, x2
        x3, y3
        ...
    x(s-1), y(s-1)
        ex, ey
```

- So the total cost = `s + k * Σ(weight(xi, yi))` where `x(s), y(s) = ex, ey` ; `x1, y1 = sx, sy`
> However this form cannot use in the Dijkstra Algorithm.
- But `s + k * Σ(weight(xi, yi))` equivalent with `Σ(1 + k * weight(xi, yi))` 
> The weight of each cell is transformed to `1 + k * original weight`
    
### 3. Path Tracing:
- After Dijkstra's algorithm finds the optimal path, it needs to be traced back from the destination to the starting point.

  - **1. Path Tracing Loop:**

  ```python
  path = [] 
    u, v = ex, ey
    path.append((u, v))
    while True:
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
  ```

  - The path tracing loop begins after the Dijkstra's algorithm has successfully found the minimum distance to the destination cell `(ex, ey)`. This loop continues until either the source cell `(sx, sy)` is reached or a maximum count (`cnt == 21`) is reached to prevent potential infinite loops.

  - A counter `cnt` is initialized to keep track of the number of iterations in the path tracing loop. This is primarily a safety measure to avoid infinite loops.

  - The direction to move from the current cell `(u, v)` to the previous cell is retrieved from the `trace` array.

  - The coordinates `(u, v)` are updated based on the retrieved direction. This essentially moves backward along the path from the current cell to the previous cell.

  - The current cell `(u, v)` is added to the `path` list. This process continues until the source cell `(sx, sy)` is reached.

  - The loop terminates if the source cell `(sx, sy)` is reached. At this point, the `path` list contains the optimal path from the source to the destination.

  - The code then prints the minimum distance to the destination cell `(ex, ey)` and the coordinates of each cell in the optimal path, effectively showing the path from the source to the destination in reverse order.

# Reasoning:
- Dijkstra's algorithm is suitable for this task because it efficiently finds the shortest path in a weighted graph. Considering both the least steps and the least power consumption involves adjusting weights based on specific conditions, which Dijkstra's algorithm can handle effectively.
- The use of a priority queue ensures that cells with lower total weights are explored first, optimizing the search for the optimal path.
- The path tracing mechanism then reconstructs the path from the destination to the starting point. The loop stops after a limited number of iterations to avoid potential infinite loops and for practicality.


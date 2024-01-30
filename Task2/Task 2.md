# Task 2 Method Explaination
**Task Summary:**
In Task 2, the goal is to find the optimal path in a complex graph where each cell in the grid has associated weights. The challenge is to navigate from a starting point (sx, sy) to an ending point (ex, ey) while considering the least number of steps and the least power consumption. The grid may contain blocked cells, and the weights for each cell are dynamic. The task involves implementing Dijkstra's algorithm to find the optimal path and then tracing this path.

**Approach:**
Certainly! Let's go through the code step by step, explaining each part in detail:

### 1. Input Reading:

```python
n, m, k =  map(int,(input().split()))
```

- Reads the dimensions of the grid (`n` rows and `m` columns) and the number of blocked cells (`k`).

### 2. Direction Arrays:

```python
dx = np.array([0, -1, 0, 1])
dy = np.array([-1, 0, 1, 0])
dd = np.array([2, 3, 0, 1]) 
```

- `dx` and `dy` represent the possible movements in the x and y directions.
- `dd` represents the corresponding directions in terms of indices (0: left, 1: up, 2: right, 3: down).

### 3. Arrays Initialization:

```python
distance = np.full((n, m), int(1e9), dtype=int) 
weight = np.full((n, m), -1, dtype=int)
trace = np.zeros((n, m), dtype=int)
```

- `distance`: Represents the minimum distance to reach each cell. Initialized to a large value (`int(1e9)`) initially.
- `weight`: Represents the weights of each cell. Initialized to -1, indicating unweighted cells.
- `trace`: Used to trace the path back from the destination to the source.

### 4. Blocked Cells Initialization:

```python
for i in range(k):
    u, v = map(int, input().split()) 
    weight[u][v] = -2  # (u, v) is blocked
```

- Reads the coordinates of blocked cells and marks them with a weight of -2.

### 5. Source and Destination Initialization:

```python
sx, sy, ex, ey = map(int, input().split())
distance[sx][sy] = 0
```

- Reads the coordinates of the source (`sx`, `sy`) and destination (`ex`, `ey`) cells.
- Initializes the distance to the source as 0.

### 6. Weight Initialization:

```python
h = int(input())
for i in range(h):
    u, v, w = map(int, input().split())
    weight[u][v] = w 
```

- Reads additional weights for specific cells (`u`, `v`) with values `w`.

### 7. `j` and `k` Initialization:

```python
j, k = map(int, input().split())
```

- Reads the values of `j` and `k`.
### 8. Dijkstra's Algorithm:

  - **1. Initialization:**

  ```python
  heap = [(0, (sx, sy))]
  ```

  The algorithm starts with a priority queue (`heap`) containing a tuple `(0, (sx, sy))`. This tuple represents the source cell `(sx, sy)` and its distance from itself, which is 0.

  - **2. Main Loop:**

  ```python
  while heap:
      current_distance, current_cell = hq.heappop(heap)
  ```

  The main loop continues as long as there are cells in the priority queue. In each iteration, the cell with the smallest known distance (`current_distance`) is extracted from the priority queue. The tuple `(current_distance, current_cell)` represents the current state of the algorithm.
  - **3. Node Exploration:**

  ```python
  u, v = current_cell[0], current_cell[1]

  if distance[u][v] < current_distance:
      continue
  ```

  It checks whether the current cell `current_cell` has already been processed. If it has, the iteration is skipped because a shorter path to that cell has already been found.

  - **4. Neighboring Cells Exploration:**

  ```python
  for i in range(4):
      x = u + dx[i]
      y = v + dy[i]
  ```

  The algorithm explores the four possible neighboring cells of the current cell `(u, v)`.

  - **5. Validity Checks:**

  ```python
  if x < 0 or x >= n or y < 0 or y >= m:
      continue

  if weight[x][y] == -2:
      continue
  ```

  It checks whether the neighboring cell `(x, y)` is within the grid boundaries and is not blocked. If the cell is out of bounds or blocked, the iteration is skipped.

  - **6. Updating Distances:**

  ```python
  w = weight[x][y]

  if w == -1:
      w = j
  w = k * w + 1
  ```

  It retrieves the weight of the neighboring cell `(x, y)`. If the cell is unweighted (`w == -1`), it is assigned the default weight `j`. The weight is then updated to `k * w + 1`.

  - **7. Relaxation:**

  ```python
  if current_distance + w < distance[x][y]:
      distance[x][y] = current_distance + w
      trace[x][y] = dd[i]
      hq.heappush(heap, (current_distance + w, (x, y)))
  ```

  If the new calculated distance from the starting cell `(sx, sy)` to the neighboring cell `(x, y)` is shorter than the currently known distance, the following updates occur:
  - `distance[x][y]` is updated to the new shorter distance.
  - `trace[x][y]` is updated to store the direction to reach `(x, y)` from the current cell `(u, v)`.
  - The neighboring cell `(x, y)` is added back to the priority queue for further exploration.
 
### 9. Path Tracing:
- After Dijkstra's algorithm finds the optimal path, it needs to be traced back from the destination to the starting point.

  - **1. Path Tracing Loop:**

  ```python
  while True:
      cnt += 1

      if cnt == 21:
          break

      dir = trace[u][v]
      x = u + dx[dir]
      y = v + dy[dir]

      u, v = x, y
      path.append((u, v))

      if (u == sx and v == sy):
          break
  ```

  The path tracing loop begins after the Dijkstra's algorithm has successfully found the minimum distance to the destination cell `(ex, ey)`. This loop continues until either the source cell `(sx, sy)` is reached or a maximum count (`cnt == 21`) is reached to prevent potential infinite loops.

  - **2. Count Initialization:**

  ```python
  cnt = 0
  ```

  A counter `cnt` is initialized to keep track of the number of iterations in the path tracing loop. This is primarily a safety measure to avoid infinite loops.

  - **3. Direction Retrieval:**

  ```python
  dir = trace[u][v]
  ```

  The direction to move from the current cell `(u, v)` to the previous cell is retrieved from the `trace` array.

  - **4. Coordinate Updates:**

  ```python
  x = u + dx[dir]
  y = v + dy[dir]

  u, v = x, y
  ```

  The coordinates `(u, v)` are updated based on the retrieved direction. This essentially moves backward along the path from the current cell to the previous cell.

  - **5. Path Building:**

  ```python
  path.append((u, v))
  ```

  The current cell `(u, v)` is added to the `path` list. This process continues until the source cell `(sx, sy)` is reached.

  - **6. Exit Condition:**

  ```python
  if (u == sx and v == sy):
      break
  ```

  The loop terminates if the source cell `(sx, sy)` is reached. At this point, the `path` list contains the optimal path from the source to the destination.

  - **7. Output:**

  ```python
  # Output
  print(distance[ex][ey])
  for cell in path[::-1]:
      print(cell[0], cell[1])
  ```

  The code then prints the minimum distance to the destination cell `(ex, ey)` and the coordinates of each cell in the optimal path, effectively showing the path from the source to the destination in reverse order.

### Reasoning:
- Dijkstra's algorithm is suitable for this task because it efficiently finds the shortest path in a weighted graph. Considering both the least steps and the least power consumption involves adjusting weights based on specific conditions, which Dijkstra's algorithm can handle effectively.
- The use of a priority queue ensures that cells with lower total weights are explored first, optimizing the search for the optimal path.
- The path tracing mechanism then reconstructs the path from the destination to the starting point. The loop stops after a limited number of iterations to avoid potential infinite loops and for practicality.

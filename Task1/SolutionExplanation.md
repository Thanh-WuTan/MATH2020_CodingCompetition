# Task 1 Method Explaination
**Task Summary:**
The task involves finding the most efficient path from point A to point B in a grid. The grid is represented as a simple graph, and the movement is allowed to adjacent cells in up, down, left, or right directions. Some cells in the grid may be blocked, and the mission is to navigate from the starting point (sx, sy) to the ending point (ex, ey) while avoiding blocked cells.

**Approach:**
The provided code implements a Breadth-First Search (BFS) algorithm to find the path from the starting point to the ending point in the given grid. Here's a breakdown of the approach:

1. **Initialization:**
   - `dx`, `dy`, and `dd` are arrays representing changes in x, y, and direction for each movement (left, up, right, down).
   - `is_visited` is a 2D array to keep track of visited cells.
   - `trace` is another 2D array to store the trace of the path.
   - The grid is initialized with blocked cells based on the input.

2. **Breadth-First Search (BFS):**

      **Objective:** The BFS algorithm is employed to explore the grid systematically and find the shortest path from the starting point to the ending point.

      **Initialization:**
      - `Q` is a queue that will be used to keep track of cells to be explored.
      - `l` and `r` are pointers representing the left and right boundaries of the queue.
      - `is_visited` is a 2D array to mark cells as visited.
      - `trace` is another 2D array to store the trace of the path.

      **Algorithm:**
      + The starting point `(sx, sy)` is added to the queue, and `l` and `r` are initialized to 0.
      + While there are cells to explore (`l <= r`), the algorithm continues:
         - Dequeue the cell `(u, v)` from the front of the queue.
         - If `(u, v)` is the destination point `(ex, ey)`, break out of the loop.
         - Otherwise, explore the four adjacent cells:
         - If the adjacent cell is within the grid boundaries and has not been visited or blocked, mark it as visited, record the direction in the `trace` array, and enqueue the cell.
         - Increment `l` to move to the next cell in the queue.

         **Code:**
         ```python
         while l <= r:
            u, v = Q[l][0], Q[l][1]
            l += 1
            if u == ex and v == ey:
               break
            for i in range(4):
               x = u + dx[i]
               y = v + dy[i]
               if x < 0 or x >= n or y < 0 or y >= m:  # Out of the boundary
                     continue
               if is_visited[x][y]:  # is already visited or is blocked
                     continue

               is_visited[x][y] = True
               trace[x][y] = dd[i]
               Q.append((x, y))
               r += 1
         ```

3. **Path Tracing:**

   **Objective:** Once the BFS exploration is complete, the path needs to be traced from the destination back to the starting point.

   **Algorithm:**
   + Initialize an empty list `res` to store the cells in the path.
   + Starting from the destination `(ex, ey)`, trace back to the starting point:
      - At each step, determine the direction of the previous cell using the `trace` array.
      - Update the current cell to the previous cell and add it to the `res` list.
   + Continue this process until the starting point `(sx, sy)` is reached.

      **Code:**
      ```python
      # Trace the path
      res = []
      x, y = ex, ey
      res.append((x, y))
      while x != sx or y != sy:
         dir = trace[x][y]
         xx = x + dx[dir]
         yy = y + dy[dir]
         res.append((xx, yy))
         x, y = xx, yy
      ```

4. **Result Output:**
   - The code generates an output file for each input file in the './result/' directory.
   - The output file contains the length of the path and the coordinates of each cell in the path, printed in reverse order.

**Reasoning:**
BFS is chosen for this task because it efficiently explores paths in a systematic order, ensuring the shortest path is found. The use of a queue (`Q`) helps in exploring cells level by level, and the trace array allows reconstructing the path once the destination is reached. The code also ensures that out-of-bound and already visited or blocked cells are not explored, optimizing the search process. The resulting path is then printed to an output file in the required format. Overall, BFS is a suitable choice for finding the most efficient path in a grid-like structure.
Certainly! Let's delve into the details of the BFS algorithm and the path tracing process in the given code:





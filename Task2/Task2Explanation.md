# Task 2 Method Explaination

1. **Problem**: The code solves the problem of finding the shortest path in a grid from a source cell `(sx, sy)` to a destination cell `(ex, ey)`. The grid can have blocked cells and cells with different weights. The cost of a path is defined as `s + k * c`, where `s` is the number of steps, `k` is a constant, and `c` is the sum of the weights of the cells in the path.

2. **Approach**: The code uses Dijkstra's algorithm to find the shortest path. Dijkstra's algorithm is a greedy algorithm that finds the path with the minimum distance from the source to the destination. However, the cost `s + k * c` cannot be used directly in Dijkstra's algorithm, because it is not consistent with the principle of optimality. That is, the optimal path may not be composed of optimal subpaths.

3. **Observation**: Assume that the optimaized road includes the s cells with the coordinate form as below:
```
        sx, sy
        x2, x2
        x3, y3
        ...
        x(s-1), y(s-1)
        ex, ey
```

- So the total cost = `s + k * Σ(weight(xi, yi))` where `x(s), y(s) = ex, ey` ; `x1, y1 = sx, sy`
However this form cannot use in the Dijkstra Algorithm.
- Observe that, `s + k * Σ(weight(xi, yi))` equivalent with `Σ(1 + k * weight(xi, yi))` 
4. **Final solution**: As reasoning above, if we change the weight of each cell to `1 + k * original weight`, the most optimal path found by Dijikstra with the new weight will achieve the goal of the problem.

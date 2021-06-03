# Shortest Cell Path
# In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

# Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

# It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

# If the task is impossible, return -1.

# Examples:

# input:
# grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
# sr = 0, sc = 0, tr = 2, tc = 0
# output: 8
# (The lines below represent this grid:)
# 1111
# 0001
# 1111

# grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
# sr = 0, sc = 0, tr = 2, tc = 0
# output: -1
# (The lines below represent this grid:)
# 1111
# 0001
# 1011
# Constraints:

# [time limit] 5000ms
# [input] array.array.integer grid
# 1 ≤ arr.length = arr[i].length ≤ 10
# [input] integer sr
# [input] integer sc
# [input] integer tr
# [input] integer tc
# All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
# [output] integer

# Hints
# What algorithms might be useful for finding a shortest distance?

# We should use a breadth-first search.

# Typically in a breadth first search, there is some graph, which for each node has some number of neighbors.

# How could we build a graph from the input that would represent the distances described in the question well?

# Here, the nodes are locations in the grid, the neighbors are adjacent locations (4-directionally) that are on the grid and have value 1.

# Solution: Breadth-First Search

# Finding a shortest path is typically done with a breadth first search. Here, nodes are locations on the grid with value 1, and two nodes are neighbors if they are 4-directionally adjacent.

# The breadth first search algorithm is given a source in the graph, and it explores all nodes distance 0 from the source, then all nodes distance 1, then all nodes distance 2, and so on. The algorithm records the node’s distance when it visits, and that way we can determine the shortest path in the graph to some target node.

# By visiting nodes in order from distance to the source, this ensures that if we find the target word, we found it at the least possible distance and thus the answer is correct.

# function shortestCellPath(grid, sr, sc, tr, tc):
#     queue = Queue()
#     queue.add((sr, sc, 0))
#     seen = new HashSet()
#     seen.add((sr, sc))

#     while queue:
#         r, c, depth = queue.popfront()
#         if r == tr and c == tc: return depth
#         for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
#             if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
#                 queue.append((nr, nc, depth + 1))
#                 seen.add((nr, nc))

#     return -1
# Time Complexity: O(R*C), where R, C are the number of rows and columns in grid. We might visit every square in the grid. It’s worth noting that typically in a breadth-first-search, the time complexity is O(V+E) where V = R * C is the number of nodes in the graph, and E is the number of edges. Since E <= 4*V, this is O(V+E) = O(V) = O(R * C).

# Space Complexity: O(R*C), the space to store queue and seen.


from collections import deque


def shortestCellPath(grid, sr, sc, tr, tc):

    # a solution is to use breath-first search

    pathq = deque()
    pathq.append((sr, sc, 0))
    visited = set()
    visited.add((sr, sc))

    while pathq:
        r, c, depth = pathq.pop()
        print(r, c, depth)
        if r == tr and c == tc:
            return depth
        for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                pathq.append((nr, nc, depth+1))
                visited.add((nr, nc))

    return -1

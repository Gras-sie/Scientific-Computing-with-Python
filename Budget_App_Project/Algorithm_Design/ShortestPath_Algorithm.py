"""
PYTHON SHORTEST PATH ALGORITHMS CHEAT SHEET:

GRAPH REPRESENTATIONS:
- Adjacency List: Dictionary where keys are nodes and values are lists of neighbors
    graph = {
        'A': [('B', 1), ('C', 4)],  # Node A connects to B (weight 1) and C (weight 4)
        'B': [('C', 2), ('D', 5)],
        # ...
    }
- Adjacency Matrix: 2D array where matrix[i][j] represents edge weight from node i to j

DIJKSTRA'S ALGORITHM:
- Purpose: Find shortest path from a start node to all other nodes in a weighted graph
- Time Complexity: O(E log V) with priority queue
- Key Components:
  * Priority Queue: Efficiently select the next closest unvisited vertex
  * Distance Dictionary: Track shortest known distance to each node
  * Visited Set: Track which nodes have been fully processed

BFS (BREADTH-FIRST SEARCH):
- Purpose: Find shortest path in unweighted graph
- Uses a queue to visit nodes in order of distance from start
- Time Complexity: O(V + E)

A* ALGORITHM:
- Improved version of Dijkstra's using heuristics
- Uses a priority queue with f(n) = g(n) + h(n) where:
  * g(n) is the cost from start to current node
  * h(n) is the estimated cost from current node to goal

FLOYD-WARSHALL ALGORITHM:
- Purpose: Find shortest paths between all pairs of nodes
- Works with positive and negative edge weights (no negative cycles)
- Time Complexity: O(V³)

BELLMAN-FORD ALGORITHM:
- Purpose: Find shortest paths from a single source
- Can handle negative edge weights
- Time Complexity: O(V × E)
- Can detect negative weight cycles

IMPLEMENTING DIJKSTRA'S ALGORITHM:
```python
import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue to get the nearest unvisited node
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've found a longer path, ignore it
        if current_distance > distances[current_node]:
            continue
            
        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances
```
"""

# Placeholder for your ShortestPath algorithm implementation
# Example implementation of Dijkstra's algorithm could go here

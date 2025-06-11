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
"""
"""
import heapq  # Used for the priority queue in Dijkstra's algorithm

def dijkstra(graph, start):
    # This function implements Dijkstra's Algorithm to find the shortest distance
    # from a 'start' node to every other node in a weighted graph.
    # 'graph' is assumed to be a dictionary where the keys are node labels
    # and each value is a list of tuples (neighbor, weight).
    
    # Initialize distances for each node to infinity, except the start node which is set to 0.
    # This dictionary will keep track of the minimum cost to reach each node from 'start'.
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # The priority queue is a min-heap where items are in (distance, node) format.
    priority_queue = [(0, start)]
    
    # While there are still nodes in the priority queue, pop the one with the smallest distance
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've found a longer path, ignore it
        if current_distance > distances[current_node]:
            continue
            
        # Otherwise, for each neighbor of the current node, calculate a new possible distance.
        # If the new distance is smaller than what's recorded, update and push to the priority queue.
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances  # Return the dictionary containing each node's shortest distance from 'start'.
"""
my_graph = {
    # Graph dictionary where each key is a node label
    # and the values are lists of (neighbor, edge_weight).
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # This function attempts to find the shortest distance and path from 'start'
    # to all other nodes in 'graph'. If a specific 'target' is provided, it focuses
    # on returning or printing information for that single node.
    
    # unvisited: List of all nodes that haven't been "finalized" yet.
    unvisited = list(graph)
    # distances: Dictionary storing the shortest distances from 'start' to each node.
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # paths: Dictionary storing the actual path taken to reach each node from 'start'.
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        # 'current' is the unvisited node with the smallest known distance from 'start'.
        current = min(unvisited, key = distances.get)
        # If the smallest distance is infinity, it means we can't reach any more nodes.
        if distances[current] == float('inf'):
            break
        for node, distance in graph[current]:
            # For each neighbor of the current node, see if going through 'current' yields
            # a shorter path than what's recorded. Update distances and paths if so.
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                # If 'paths[node]' is empty or the last node in the path is not 'node',
                # we need to create a new path for 'node' since we are building it from 'current'.
                if paths[node] and paths[node][-1] == node:
                # If 'paths[node]' is empty, we initialize it with the path leading to 'current'.
                    # This means we are starting a new path to 'node' from 'current'.
                    paths[node] = paths[current][:]
                # If 'paths[node]' is not empty and the last node is 'node', we extend it.
                # This means we are already building a path to 'node' and we can extend it.
                else:
                # Extend the path leading to 'node' with the path leading to 'current'.
                # This ensures we build the path correctly from 'start' to 'node'.
                    paths[node].extend(paths[current])
                # Append the current node to the path leading to 'node'.
                paths[node].append(node)
        # Once we've considered all neighbors, 'current' can be removed from unvisited.
        unvisited.remove(current)
    # targets_to_print is determined by whether 'target' was provided.
    targets_to_print = [target] if target else graph
    # If 'target' is not specified, we will print details for all nodes in the graph.
    if target and target not in graph:
        # If the target node is not in the graph, we raise an error.
        raise ValueError(f"Target node '{target}' not found in the graph.")
    
    for node in targets_to_print:
        # If 'node' is the start node, we skip printing details about it.
        # This is to avoid showing trivial information about the start node.
        if node == start:
            # Skip printing details about the start node so we don't show trivial info.
            continue
        # Print the distance to the node, and the path to reach it, separated by '->'.
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths  # Return both distances and paths for further processing if needed.

# Example usage of the shortest_path function
shortest_path(my_graph, 'A', 'F')

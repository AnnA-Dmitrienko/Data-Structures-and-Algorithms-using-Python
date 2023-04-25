


# Heap queue is a special tree structure in which each parent node is less than or equal to its child node.
import heapq


def dijkstra(graph, start, target):
    # Create a dictionary called distances that will store the distances between the start node and all other nodes in the graph.
    distances = {node: float('inf') for node in graph}
    # Set the distance of the start node to 0 and the distance of all other nodes to infinity
    distances[start] = 0
    # Create a priority queue called unvisited that will store the unvisited nodes in the graph.
    # Insert the start node with a priority of 0.
    unvisited = [(0, start)]
    # Create a dictionary called previous that will store the previous node in the shortest path to each node.
    previous = {node: None for node in graph}

    # While unvisited is not empty, do the following:
    while (unvisited):
        # Pop the node with the lowest priority from `unvisited`.- using heappop method of heap queue
        current_distance, current_node = heapq.heappop(unvisited)
        # If the node is the target node, stop the algorithm and return the shortest path and its distance.
        if (current_node == target):
            shortest_path = []
            while (current_node):
                shortest_path.append(current_node)
                # go to the previous node with the next lowest priority
                current_node = previous[current_node]
                # 2 values to return - 1) distance to target 2) shortest path
                current_distance = reversed(shortest_path)
            return print(f'The shortest path from {start} to {target} is: {list(current_distance)}'),\
                print(
                    f'The distance from {start} to {target} is : {distances[target]}')

        # For each neighbor of the current node, calculate the tentative distance from the start node to the neighbor.
        for neighbour_node, added_distance in graph[current_node].items():
            temp_distance = distances[current_node] + added_distance
            # If the tentative distance is less than the current distance stored in `distances`, update `distances` and `previous`.
            if (temp_distance < distances[neighbour_node]):
                distances[neighbour_node] = temp_distance
                previous[neighbour_node] = current_node
                # Add the neighbor to `unvisited` with a priority equal to the tentative distance.
                heapq.heappush(unvisited, (temp_distance, neighbour_node))

    # If the target node is not reached, return None.
    return None


# Driver code- TESTING:

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}


# from A to F, B, G
print("TESTING \"A\" as start:")
dijkstra(graph, 'A', 'F')
dijkstra(graph, 'A', 'B')
dijkstra(graph, 'A', 'G')
print("\n")

# from B to D, C, F, G
print("TESTING \"B\" as start:")
dijkstra(graph, 'B', 'B')
dijkstra(graph, 'B', 'D')
dijkstra(graph, 'B', 'C')
dijkstra(graph, 'B', 'F')
dijkstra(graph, 'B', 'G')
print("\n")


print("TESTING \"F\" as start:")
dijkstra(graph, 'F', 'B')
dijkstra(graph, 'F', 'G')
dijkstra(graph, 'F', 'A')

# OUTPUT:
# TESTING "A" as start:
# The shortest path from A to F is: ['A', 'B', 'D', 'F']
# The distance from A to F is : 5
# The shortest path from A to B is: ['A', 'B']
# The distance from A to B is : 2
# The shortest path from A to G is: ['A', 'B', 'D', 'F', 'G']
# The distance from A to G is : 8


# TESTING "B" as start:
# The shortest path from B to B is: ['B']
# The distance from B to B is : 0
# The shortest path from B to D is: ['B', 'D']
# The distance from B to D is : 1
# The shortest path from B to C is: ['B', 'C']
# The distance from B to C is : 2
# The shortest path from B to F is: ['B', 'D', 'F']
# The distance from B to F is : 3
# The shortest path from B to G is: ['B', 'D', 'F', 'G']
# The distance from B to G is : 6


# TESTING "F" as start:
# The shortest path from F to B is: ['F', 'D', 'B']
# The distance from F to B is : 3
# The shortest path from F to G is: ['F', 'G']
# The distance from F to G is : 3
# The shortest path from F to A is: ['F', 'D', 'B', 'A']
# The distance from F to A is : 5

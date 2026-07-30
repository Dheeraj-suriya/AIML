from collections import deque

# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        # Print each visited node
        print("Visited:", current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Find shortest path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nBFS Traversal Path:")
    print(" -> ".join(path))

# Main
bfs(graph, "Alice", "Bob")
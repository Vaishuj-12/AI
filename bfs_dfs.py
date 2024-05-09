from collections import defaultdict, deque

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_iterative(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function to build an undirected graph from user input
def build_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges (e.g., 'u v' without quotes) separated by space:")
    for _ in range(num_edges):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph, so add both directions
    
    return graph

# Main program to perform DFS and BFS traversal
if __name__ == "__main__":
    graph = build_graph()
    start = input("Enter the start node for traversal: ")
    
    print("\nDFS (Recursive) traversal starting from node '{}':".format(start))
    dfs_recursive(graph, start,visited=None)
    print()  # Print a new line for clarity
    
    print("\nBFS (Iterative) traversal starting from node '{}':".format(start))
    bfs_iterative(graph, start)
    print()  # Print a new line for clarity

def is_valid(graph, vertex, color, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, num_vertices):
    colors = [-1] * num_vertices  # Array to store assigned colors
    
    def backtrack(current_vertex):
        if current_vertex == num_vertices:
            return True
        
        for color in range(1, num_vertices + 1):  # Try colors 1 to num_vertices
            if is_valid(graph, current_vertex, color, colors):
                colors[current_vertex] = color
                if backtrack(current_vertex + 1):
                    return True
                colors[current_vertex] = -1  # Backtrack
            
        return False
    
    if backtrack(0):
        return colors
    else:
        return None

def main():
    # Input number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    # Initialize graph as adjacency list
    graph = [[] for _ in range(num_vertices)]
    
    # Input the edges
    print("Enter the edges (format: u v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Solve graph coloring
    coloring = graph_coloring(graph, num_vertices)
    
    if coloring:
        print("Vertex colors:")
        for vertex, color in enumerate(coloring):
            print(f"Vertex {vertex}: Color {color}")
    else:
        print("No valid coloring exists.")

if __name__ == "__main__":
    main()

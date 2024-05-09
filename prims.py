# The algorithm starts with an empty spanning tree. 
# The idea is to maintain two sets of vertices. 
# The first set contains the vertices already 
# included in the MST, and the other set contains 
# the vertices not yet included. At every step, 
# it considers all the edges that connect the two 
# sets and picks the minimum weight edge from these 
# edges. After picking the edge, it moves the other 
# endpoint of the edge to the set containing MST. 

INF = 9999999

# Take input for the number of nodes (N)
N = int(input("Enter the number of nodes: "))

# Initialize the graph adjacency matrix
G = []
print("Enter the adjacency matrix for the graph (N x N):")
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)

# Initialize selected_node array and other variables
selected_node = [False] * N
no_edge = 0
selected_node[0] = True


print("Edge : Weight\n")
while no_edge < N - 1:
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if not selected_node[n] and G[m][n] > 0:  # Check if there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(f"{a}-{b}: {G[a][b]}")
    selected_node[b] = True
    no_edge += 1
    
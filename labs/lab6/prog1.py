def createGraph(file):
    G = {}
    with open(file, "r") as f:
        for line in f:
            node = int(line.split()[0])
            edge = int(line.split()[1])
            if node not in G:
                G[node] = []
            G[node].append(edge)
    return G


def reverseGraph(graph):
    G_r = {}

    for i in graph:
        for n in graph[i]:
            if n not in G_r:
                G_r[n] = []
            G_r[n].append(i)
    return G_r


def mark(G, v, visited, order):
    # dont go in visited nodes
    if v in visited:
        return order
    # mark visited with preorder
    visited[v] = [order, None]
    order += 1

    if v in G:
        node = G[v]
        # go to each neighbor node and explore it if we haven't visited it
        backtrack = True
        for neighbor in node:
            if neighbor not in visited:
                backtrack = False
                # track the order
                order = mark(G, neighbor, visited, order)
        if backtrack:
            # if all neighbors have been visited, mark the node with its postorder
            visited[v][1] = order
            order += 1
    # nodes with no neighbors
    # mark it with its postorder
    if visited[v][1] is None:
        visited[v][1] = order
        order += 1
    return order




if __name__ == "__main__":
    # filename = input("Enter a filename: ")
    filename = "LAB6-TEST-SET.txt"
    G = createGraph(filename)
    G_r = reverseGraph(G)
    print(G)
    # print(G_r)
    # print("G_r")
    # for node in G_r:
    visited = {}
    mark(G, 1, visited, 1)
    print(visited)

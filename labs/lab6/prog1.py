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


def explore(G, v, visited):
    # if we have visited the node we are at in the graph, don't go down it's path
    if v in visited:
        return
    # add the node to visited since we are going down it's path
    visited.append(v)
    # look at what else the node points to
    if v in G:
        node = G[v]
        # go to each neighbor node and explore it if we haven't visited it
        for neighbor in node:
            if neighbor not in visited:
                explore(G, neighbor, visited)
    return visited


if __name__ == "__main__":
    filename = input("Enter a filename: ")
    G = createGraph(filename)
    G_r = reverseGraph(G)
    # print(G)
    # print(G_r)
    print("G_r")
    for node in G_r:
        print(explore(G_r, node, []))
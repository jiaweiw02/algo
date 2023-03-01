from heapdict import heapdict


def readFile(file):
    hd = heapdict()
    with open(file, "r") as f:
        for line in f:
            node1 = int(line.split()[0])
            node2 = int(line.split()[1])
            weight = int(line.split()[2])
            key_ = (node1, node2)
            hd[key_] = weight
    return hd


def dijkstra(graph, start):
    dist = {}
    prev = {}
    for key in graph:
        node1 = key[0]
        node2 = key[1]
        dist[node1] = float("inf")
        dist[node2] = float("inf")

        prev[node1] = None
        prev[node2] = None
    dist[start] = 0

    H = heapdict()
    for key in dist:
        H[key] = dist[key]

    while H:
        (u, distance) = H.popitem()

        for key in graph:
            if key[0] != u:
                continue

            v = key[1]
            if dist[v] > dist[u] + graph[key]:
                dist[v] = dist[u] + graph[key]
                prev[v] = u
                # decrease key
                H[v] = dist[u] + graph[key]

        # print shortest distance and path for current node
        path = [u]
        if u != start:
            node = u
            while node != start:
                if node is None:
                    break
                path.append(prev[node])
                node = prev[node]
        r_path = [path[i] for i in range(len(path) - 1, -1, -1)]
        print("{}: {}: {}".format(u, dist[u], r_path))


if __name__ == "__main__":
    F = input("Enter a filename: ")
    sNode = int(input("Enter a starting node: "))
    g = readFile(F)
    dijkstra(g, sNode)

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


def createOrdering(orderings, max_post):
    # create an array of size max_post
    arr = [0 for i in range(max_post)]

    for node in orderings:
        index = orderings[node][1] - 1
        arr[index] = node

    return arr


def mark(G, v, visited, order, max_post):
    # dont go in visited nodes
    if v in visited:
        return order
    # mark visited with preorder
    visited[v] = [order, None]
    if order > max_post[0]:
        max_post[0] = order
    order += 1

    if v in G:
        node = G[v]
        # go to each neighbor node and explore it if we haven't visited it
        backtrack = True
        for neighbor in node:
            if neighbor not in visited:
                backtrack = False
                # track the order
                order = mark(G, neighbor, visited, order, max_post)
        if backtrack:
            # if all neighbors have been visited, mark the node with its postorder
            visited[v][1] = order
            if order > max_post[0]:
                max_post[0] = order
            order += 1
    # nodes with no neighbors
    # mark it with its postorder
    if visited[v][1] is None:
        visited[v][1] = order
        if order > max_post[0]:
            max_post[0] = order
        order += 1
    return order


def dfs(G, starting_node, visited, checked):
    if starting_node in visited:
        return
    if starting_node in checked:
        return
    if starting_node not in G:
        return
    visited.append(starting_node)

    for n in G[starting_node]:
        if n not in visited:
            dfs(G, n, visited, checked)
    return visited


if __name__ == "__main__":
    # filename = input("Enter a filename: ")
    filename = "example.txt"
    G = createGraph(filename)
    G_r = reverseGraph(G)
    visited = {}
    postOrder = [0]
    mark(G, 1, visited, 1, postOrder)
    post_order = createOrdering(visited, postOrder[0])
    print(post_order)
    checked = []
    for post in range(len(post_order)-1, -1, -1):
        node = post_order[post]
        # if checked already, don't check
        if node in checked:
            continue
        # marking everything connected to me
        visited_r = []
        dfs_arr = dfs(G_r, node, visited_r, checked)
        if dfs_arr is not None:
            checked += dfs_arr
        print(node, visited_r)

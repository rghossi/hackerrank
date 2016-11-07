# Enter your code here. Read input from STDIN. Print output to STDOUT
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
                
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def insertEdge(graph, n1, n2):
    graph[n1].add(n2)
    graph[n2].add(n1)

q = int(raw_input())

for i in range(q):
    graph = {}
    n_temp = raw_input().split(" ")
    n_temp = map(int, n_temp)
    n = n_temp[0]
    m = n_temp[1]
    for j in range(n):
        graph[j+1] = set()
    for j in range(m):
        node_temp = raw_input().split(" ")
        node_temp = map(int, node_temp)
        insertEdge(graph, node_temp[0], node_temp[1])
    s = int(raw_input())
    line = ""
    for key in sorted(graph):
        if (s == key): continue
        n_path = shortest_path(graph, s, key)
        if (n_path == None): n_path = -1
        else: n_path = (len(n_path)-1) * 6
        line += " " + str(n_path)
    print(line.strip())
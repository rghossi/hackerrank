# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def bfs_paths(graph, start):
    visited, queue = set(), [(start, [start])]
    paths_len = {}
    for j in range(len(graph)):
        paths_len[j+1] = None
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for next in graph[vertex] - set(path):
                queue.append((next, path + [next]))
                if (paths_len[next] == None or paths_len[next] > len(path)):
                    paths_len[next] = len(path)
    return paths_len

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
    paths = bfs_paths(graph, s)
    for k,v in sorted(paths.iteritems()):
        if k == s: continue
        if v == None: v = -1
        else: v *= 6
        line += str(v) + " "
    print(line.strip())
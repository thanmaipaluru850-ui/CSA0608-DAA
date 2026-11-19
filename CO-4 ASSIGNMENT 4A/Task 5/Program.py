# Task 5: Dijkstra, Bellman-Ford and Floyd-Warshall
INF = float("inf")

def dijkstra(vertices, edges, source):
    graph = {v: [] for v in vertices}
    for u, v, w in edges:
        if w < 0:
            raise ValueError("Dijkstra requires non-negative edge weights")
        graph[u].append((v, w))
    dist = {v: INF for v in vertices}
    pred = {v: None for v in vertices}
    visited = set()
    dist[source] = 0

    while len(visited) < len(vertices):
        candidates = [v for v in vertices if v not in visited]
        u = min(candidates, key=lambda v: dist[v])
        if dist[u] == INF:
            break
        visited.add(u)
        for v, weight in graph[u]:
            if v not in visited and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
    return dist, pred

def bellman_ford(vertices, edges, source):
    dist = {v: INF for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None, None, True
    return dist, pred, False

def floyd_warshall(vertices, edges):
    dist = {u: {v: (0 if u == v else INF) for v in vertices}
            for u in vertices}
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == "__main__":
    V = ["A", "B", "C", "D", "E"]
    E = [("A","B",4), ("A","C",7), ("B","C",2),
         ("B","D",6), ("C","D",1), ("D","E",3), ("C","E",8)]
    distances, predecessors = dijkstra(V, E, "A")
    print("Dijkstra distances:", distances)
    print("Dijkstra predecessors:", predecessors)
    bf_dist, _, cycle = bellman_ford(V, E, "A")
    print("Bellman-Ford negative cycle:", cycle)
    print("Bellman-Ford distances:", bf_dist)
    print("Floyd-Warshall matrix:")
    for vertex in V:
        print(vertex, floyd_warshall(V, E)[vertex])
  

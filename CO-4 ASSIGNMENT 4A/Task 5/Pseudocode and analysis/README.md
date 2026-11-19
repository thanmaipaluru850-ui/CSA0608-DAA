Task 5 – Dijkstra, Bellman-Ford and Floyd Algorithms
1. Graph
Directed weighted edges:

A→B(4), A→C(7), B→C(2), B→D(6), C→D(1), D→E(3), C→E(8).
2. Dijkstra from source A
All weights are non-negative, so the unsettled vertex with the smallest tentative distance can be permanently selected.

ALGORITHM Dijkstra(G, A)
BEGIN
    FOR each vertex v DO
        dist[v] <- INFINITY
        pred[v] <- NIL
        visited[v] <- FALSE
    END FOR

    dist[A] <- 0

    REPEAT |V| times
        u <- unvisited vertex with minimum dist

        IF no such finite-distance vertex exists THEN
            BREAK
        END IF

        visited[u] <- TRUE

        FOR each edge (u, v) with weight c DO
            IF visited[v] = FALSE AND dist[u] + c < dist[v] THEN
                dist[v] <- dist[u] + c
                pred[v] <- u
            END IF
        END FOR
    END REPEAT

    RETURN dist, pred
END

Manual trace Start: A=0, all others = infinity. Select A: update B=4, C=7. Select B (4): update C=min(7,4+2)=6; D=10. Select C (6): update D=min(10,6+1)=7; E=14. Select D (7): update E=min(14,7+3)=10. Select E (10): no change. Vertex Shortest distance from A Predecessor Path A 0 – A B 4 A A→B C 6 B A→B→C D 7 C A→B→C→D E 10 D A→B→C→D→E

3.Bellman-Ford for negative edges Dijkstra's permanent greedy choice becomes unsafe because a later path containing a negative edge may reduce the distance of a vertex already selected. Core pseudocode ALGORITHM BellmanFord(G, A) BEGIN Initialise all distances to INFINITY and predecessors to NIL dist[A] <- 0

 FOR i <- 1 TO |V|-1 DO changed <- FALSE FOR each edge (u, v, weight) DO IF dist[u] != INFINITY AND dist[u] + weight < dist[v] THEN dist[v] <- dist[u] + weight pred[v] <- u changed <- TRUE END IF END FOR IF changed = FALSE THEN BREAK END FOR

 FOR each edge (u, v, weight) DO IF dist[u] != INFINITY AND dist[u] + weight < dist[v] THEN RETURN "Reachable negative-weight cycle exists" END IF END FOR RETURN dist, pred END A shortest simple path contains at most |V|-1 edges, so repeated relaxation for that many rounds is sufficient when no reachable negative cycle exists. A further possible improvement indicates a reachable negative cycle.

4.Floyd's all-pairs shortest paths D^(k)[i][j] means the shortest distance from vertex i to vertex j using only vertices 1..k as intermediate vertices. Core transition FOR k <- 1 TO |V| DO FOR i <- 1 TO |V| DO FOR j <- 1 TO |V| DO D[i][j] <- MIN(D[i][j], D[i][k] + D[k][j]) END FOR END FOR END FOR Initialise D[i][j] with the edge weight, 0 when i=j, and infinity when no edge exists. Floyd considers every pair, while Dijkstra and Bellman-Ford calculate distances from one source.

5.Complexity Dijkstra with a simple array: O(V^2 + E), space O(V). Bellman-Ford: O(VE), space O(V). Floyd-Warshall: O(V^3), space O(V^2).


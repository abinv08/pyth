import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(g, start):
    dist = {v: float('inf') for v in g}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        for v, cost in g[u].items():
            nd = d + cost

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    print(f"\nRouter {start}")

    for dest in g:
        print(f"{dest}\tCost={dist[dest]}")

for router in graph:
    dijkstra(graph, router)
import heapq

network = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 3, 'D': 4},
    'C': {'A': 1, 'B': 3, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

def link_state_routing(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, cost in graph[current_node].items():
            distance = current_distance + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

source = 'A'
paths = link_state_routing(network, source)

for node in paths:
    print(node, ":", paths[node])
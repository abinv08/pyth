import copy;
nodes=['A','B','C'];
INFINITY=999;
graph = {
    'A':{'A': 0, 'B': 2, 'C': 9},
    'B':{'A': 2 ,'B':0,  'C':3 },
    'C':{'A': 9, 'B': 3, 'C':0 }
};
distance_vector = copy.deepcopy(graph);
def display(iteration):
    print(f"\Routing table after alteration {iteration}:")
    for node in nodes:
        print(f"Rounter{node}:{distance_vector[node]}");
for iteration in range(1, len(nodes) + 1):
    for src in nodes:
        for desc in nodes:
            for via in nodes:
                distance_vector[src][desc] = min(
                    distance_vector[src][desc],
                    graph[src][via]+distance_vector[via][desc]
                )
    display(iteration);

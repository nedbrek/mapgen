import networkx as nx
import random

### main
if __name__ == '__main__':
    graph = nx.Graph()

    # add nodes to the graph
    n = 10
    for i in range(n):
        graph.add_node(i)

    # until graph is connected
    while not nx.is_connected(graph):
        # connect nodes in the graph randomly
        node1 = random.randint(0, n - 1)
        node2 = random.randint(0, n - 1)
        if node1 != node2:
            graph.add_edge(node1, node2, weight=1)

    for n in graph.nodes:
        print(n)
        for adj in graph.neighbors(n):
            print("   ", adj, " w", graph[n][adj]['weight'])


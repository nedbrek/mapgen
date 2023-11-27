#!/usr/bin/env python3
import networkx as nx
import random

### main
if __name__ == '__main__':
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--dot", help="Use dot format", action="store_true")
    arg_parser.add_argument("-n", "--num_nodes", nargs=1, help="Specify number of nodes in the graph", default=10)
    args = arg_parser.parse_args()

    graph = nx.Graph()

    # add nodes to the graph
    n = int(args.num_nodes[0])
    for i in range(n):
        graph.add_node(i)

    # until graph is connected
    while not nx.is_connected(graph):
        # connect nodes in the graph randomly
        node1 = random.randint(0, n - 1)
        node2 = random.randint(0, n - 1)
        if node1 != node2:
            graph.add_edge(node1, node2, weight=1)

    if args.dot:
        print("graph {")
        for n in graph.nodes:
            for adj in graph.neighbors(n):
                print("n{} -- n{} [label={}]".format(n, adj, graph[n][adj]['weight']))
        print("}")
    else:
        for n in graph.nodes:
            print(n)
            for adj in graph.neighbors(n):
                print("   ", adj, " w", graph[n][adj]['weight'])


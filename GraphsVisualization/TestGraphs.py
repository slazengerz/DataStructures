import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def showGraph(value,counter=1):
    options={
        'node_color': 'green',
        'with_labels':'True'
    }
    print(f'no of edges::{len(value)}')
    g=nx.DiGraph(seed=47) 
    g.add_edges_from(value)
    pos={}
    j=0
    for i in g.nodes:
         pos[i]=np.array([j, 0]) 
         j+=1
    nx.draw_networkx(g,pos,**options)


def simple_path(value):
    G = nx.path_graph(len(value))
    pos = nx.spring_layout(G, seed=47)  # Seed layout for reproducibility
    nx.draw(G, pos=pos)
    plt.show()


def with_pos():
    G = nx.path_graph(5)  # An example graph
    center_node = 5  # Or any other node to be in the center
    edge_nodes = set(G) - {center_node}
    # Ensures the nodes around the circle are evenly distributed
    pos = nx.line_graph(G.subgraph(edge_nodes))
    for i in range(5):
        pos[i] = np.array([i, 0])  # manually specify node position
    nx.draw(G, pos, with_labels=True)

showGraph([(7,4),(4,9),(9,10),(10,13),(13,90)])
showGraph([(7,4),(4,9),(9,10),(10,13),(13,90)])
    
##simple_path([(7,4),(4,9)])

##with_pos()


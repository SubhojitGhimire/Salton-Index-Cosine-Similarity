import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as linalg
from saltonIndex import *

# MAKING A RANDOM GRAPH OF FEW NODES
numOfNodes = 10
edgeCreationProbability = 0.4
GG = nx.erdos_renyi_graph (numOfNodes, p = edgeCreationProbability)
# GG = nx.karate_club_graph ()
edges = nx.edges (GG)
print ("GRAPH EDGE SET:")
print (edges)

# SALTON INDEX (COSINE SIMILARITY)
preds = salton_index (GG)
printPreds ("\nSALTON INDEX", preds)

# GRAPH PLOTTING
plt.figure (figsize = (15, 15))
nx.draw_networkx (GG, with_labels = 'True', node_color = 'green', alpha = 0.6)
plt.show ()
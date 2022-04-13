import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as linalg
from scipy import spatial

def findUnconnected (list, numOfNodes):
    unconnectedList = [[]]
    var = 0
    for ii in range (numOfNodes):
        for jj in range (ii+1, numOfNodes):
            if jj not in list[ii]:
                unconnectedList[var].append (ii)
                unconnectedList[var].append (jj)
                var += 1
                unconnectedList += [[]]
    unconnectedList.remove ([])
    return (unconnectedList)

def saltonList (GG):
    edges = nx.edges (GG)
    numOfNodes = GG.number_of_nodes()
    list = [[]]
    for ii in range (numOfNodes-1):
        list += [[]]
    for ii in range (numOfNodes):
        for jj in edges:
            if (jj[0] == ii):
                list [ii].append (jj[1])
            if (jj[1] == ii):
                list [ii].append (jj[0])
    print ("\nCREATING LISTS FOR EACH VERTEX CONNECTED TO LIST OF OTHER VERTICES")
    var = 0
    for ii in list:
        print ("LIST ", var, " = ", ii)
        var += 1
    unconnectedNodes = findUnconnected (list, numOfNodes)
    print ("\nTO FIND SALTON INDEX FOR FOLLOWING LISTS")
    print (unconnectedNodes)
    var = 0

    adjMatrix = [[]]
    var = 0
    for ii in range (numOfNodes):
        for jj in range (numOfNodes):
            if jj not in list [ii]:
                adjMatrix[var].append (0)
            else:
                adjMatrix[var].append (1)
        var += 1
        adjMatrix += [[]]
    adjMatrix.remove ([])

    var = 0
    for ii in unconnectedNodes:
        # cosineSimilarity = dot (adjMatrix [ii[0]], adjMatrix [ii[1]]) / (norm (adjMatrix[ii[0]]) * norm (adjMatrix[ii[1]]))
        cosineSimilarity = 1 - spatial.distance.cosine (adjMatrix [ii[0]], adjMatrix [ii[1]])
        unconnectedNodes[var].append (round (cosineSimilarity, 3))
        var += 1
    return unconnectedNodes

# MAKING A RANDOM GRAPH OF FEW NODES
numOfNodes = 5
edgeCreationProbability = 0.4
GG = nx.erdos_renyi_graph (numOfNodes, p = edgeCreationProbability)
# GG = nx.karate_club_graph ()
edges = nx.edges (GG)
print ("GRAPH EDGE SET:")
print (edges)

# SALTON INDEX (COSINE SIMILARITY)
preds = saltonList (GG)
print ("\nSALTON INDEX")
for ii in preds:
    print ("(", ii [0], ", ", ii [1], ") = ", round (ii [2], 3))

# GRAPH PLOTTING
plt.figure (figsize = (15, 15))
nx.draw_networkx (GG, with_labels = 'True', node_color = 'green', alpha = 0.6)
plt.show ()


# EXAMPLE OUTPUT:

# GRAPH EDGE SET:
#  [(0, 3), (1, 2), (1, 3), (1, 4), (3, 4)]

# SALTON INDEX
# ( 0 ,  1 ) =  0.965
# ( 0 ,  2 ) =  1
# ( 0 ,  4 ) =  0.894
# ( 2 ,  3 ) =  0.7
# ( 2 ,  4 ) =  0.894

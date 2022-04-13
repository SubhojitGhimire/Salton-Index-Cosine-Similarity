from scipy import spatial
import networkx as nx

def printPreds (index, preds):
    print (index)
    for ii in preds:
        print ("(", ii [0], ", ", ii [1], ") = ", round (ii [2], 3))

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

def salton_index (GG):
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
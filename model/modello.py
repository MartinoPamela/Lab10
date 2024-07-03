import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, year):
        nodes = DAO.getAllCountries(year)
        for n in nodes:
            self._idMap[n.CCode] = n
        self._grafo.clear()
        self._grafo.add_nodes_from(nodes)

        edges = DAO.getCountryPairs(self._idMap, year)
        for e in edges:
            self._grafo.add_edge(e._c1, e._c2)

    def numCompConnesse(self):
        return nx.number_connected_components(self._grafo)

    def getNumConfinanti(self, v):
        return len(list(self._grafo.neighbors(v)))

    def getBFSNodes(self, source):
        edges = nx.dfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def getRaggiungibiliBFS(self, n):
        tree = nx.bfs_tree(self._grafo, n)
        a = list(tree.nodes)
        a.remove(n)
        return a

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getNodes(self):
        return self._grafo.nodes


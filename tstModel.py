from model.modello import Model

mymodel = Model()
mymodel.buildGraph(2000)

print(f"The graph has {mymodel.getNumNodes()} nodes.")
print(f"The graph has {mymodel.getNumEdges()} edges.")


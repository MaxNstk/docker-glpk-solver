# Vertices são interligações entre n arestas
# Cada aresta deve necessáriamente ter uma lixeira em alguma ponta
# lixeiras são instaladas em verticess
# Grafo G = {V, E}, conjuto de vertices e arestas

from pyomo.environ import *


graph = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0],
]

# vertices: [vertices adjacentes]
graph = {
    0:[1,2],
    1:[0,2,3],
    2:[0,1,3],
    3:[1,2]
}
V=4


model = ConcreteModel()

model.var = Var([i for i in range(V)], domain=Binary)

model.obj = Objective(expr=sum(model.var[i] for i in range(V)), sense=minimize)

model.con = ConstraintList()

for k,neighbors in graph.items():
    for i in neighbors:
        model.con.add(model.var[k]+model.var[i] >= 1)

# model.con.add(model.var[i]*graph[i][j] + model.var[j]*graph[j][i] for i in range(V) for j in range(V) >= 1)                      

solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(V):
    print(f'{i+1} : -> {model.var[i]()}')


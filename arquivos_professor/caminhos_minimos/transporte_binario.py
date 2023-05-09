""" 
    ij E A = arco (ij) do conjunto de arcos A
    Fij = fluxo no arco, se passou ou não por ele, 0 ou 1
    Cij = custo do arco

    minimiza = somatório de Fij * Cij para todo ij

    Variáveris de decisão: todo fij
"""
n = 7 # fornecedores
m = 7

graph = [
    [0, 3, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 2, 0],
    [0, 0, 0, 4, 5, 0, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 12],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]
s = 0 # arco inicial
t = 6 # arco final

from pyomo.environ import *

model = ConcreteModel()

model.x = Var([i for i in range(m)], [j for j in range(n)], domain=Binary)

def objective_function(model):
    cost = 0
    for i in range(n):
        for j in range(m):
            cost += model.x[i,j] * graph[i][j]
    return cost

model.obj = Objective(rule=objective_function, sense=minimize)

model.con = ConstraintList()

for i in range(n):
    for j in range(m):
        expected = 1 if i == s else -1 if i ==t else 0
        model.con.add(sum(model.x[i,k] for k in range(m)) - sum(model[l,j] for l in range(n)) == expected)

# for i in range(n):
#     expected = 1 if i == s else -1 if i ==t else 0
#     model.con.add(sum(graph[i,j] for j in range (m)) - sum(graph[j,i] for j in range(n)) == expected)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    print()
    for j in range(n):
        print(model.y[i,j]())
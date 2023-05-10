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
    # a soma dos sucessores de i - a soma dos sucessores de j = R tem de ser:
    # 1 caso o nó atual seja o de partida, afinal somente sai um acminho dele
    # -1 se for o de chegada, afinal tem de chegar somente 1
    # 0 se for intermediário, somente chega 1 e somente sai um
    expected = 1 if i == s else -1 if i ==t else 0
    model.con.add(sum(model.x[i,j] for j in range(m)) - sum(model.x[j,i] for j in range(n)) == expected)

    for j in range(n):
        # caso o valor do caminho seja 0, não há caminho
        if graph[i][j] == 0:
            model.con.add(model.x[i,j] == 0)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    for j in range(n):
        if model.x[i,j]() == 0: continue
        print(f'{i+1}-->{j+1} - Custo: {graph[i][j]}')
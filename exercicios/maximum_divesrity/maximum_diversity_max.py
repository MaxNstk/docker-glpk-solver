# problema
# dado um numero de nós n em uma arvore, 
# desejamos selecionar um numero m de nós 
# os nós selecionados devem ser aqueles cuja
# soma das dieferenças entre cada um desses elementos seja a maior possível
# a diferença é a distancia entre dois elementos

n = 6 # n de elementos
m = 3 # n de elementos do subconunto

# matriz de adjacencia com os pesos do caminho. Se peso = 0, sem caminho
graph = [
    [0, 3, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 2, 0],
    [0, 0, 0, 4, 5, 0, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 12],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

from pyomo.environ import *

model = ConcreteModel()

model.x = Var([i for i in range(n)], domain=Binary)

# buscamos a maior variedade 
def objective_function(model):
    soma = 0
    for i in range(n-1):
        for j in range(i+1,n):
            soma+= graph[i][j] * model.x[i] * model.x[j]
    return soma

model.obj = Objective(rule=objective_function, sense=maximize)

model.con = ConstraintList()

model.con.add(sum(model.x[i] for i in range(n)) == m)

# Solução GLPK N FUNCIONA, TEM QUE USAR OUTRO, NÃO É LINEAR, PROBLEMA QUADRÁTICO
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    if model.x[i]() == 0: continue
    # print(f'{i+1} Custo: {graph[i][]}')
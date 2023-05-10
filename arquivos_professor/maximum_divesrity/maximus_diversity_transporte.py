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

# variavel para saber se esse caminho será utilizado
model.x = Var([i for i in range(n)], [j for j in range(n)], domain=Binary)

# buscamos a maior variedade 
def objective_function(model):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma+= graph[i][j] * model.x[i,j]
    return soma

model.obj = Objective(rule=objective_function, sense=maximize)

model.con = ConstraintList()

# temos de nos restingir aos elementos do subconjunto m
# os caminhos precorridoscorresponderão a quantidade nós -1
#.->.->., 3 nós, dois caminhos
model.con.add(sum(model.x[i,j] for i in range(n) for j in range(n)) == (m-1))

# caso o valor do caminho seja 0, não há caminho, restringindo a somente aqueles que existem de fato
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            model.con.add(model.x[i,j] == 0)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    for j in range(n):
        if model.x[i,j]() == 0: continue
        print(f'{i+1}-->{j+1} - Custo: {graph[i][j]}')
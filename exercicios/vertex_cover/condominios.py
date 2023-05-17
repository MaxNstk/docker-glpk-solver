# Existe um condominio com diversas estradas que se interligam
# Qual é o menor numero possível de lixeiras possível em uma estrada

n = 5
graph = [ # estradas
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

from pyomo.environ import *

model = ConcreteModel()

model.x = Var([i for i in range(n)],[j for j in range(n)], domain=Binary)

model.obj = Objective(expr=sum(model.x[i,j] for i in range(n) for j in range(n)), sense=minimize)

model.con = ConstraintList()

# se não tem interseção não pode ter lixeira
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            model.con.add(model.x[i,j] == 0)

for i in range(n):
    model.con.add(sum(model.x[i,j] for j in range(n)) == 1)
    model.con.add(sum(model.x[j,i] for j in range(n)) == 1)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    if model.x[i]() == 0: continue
    print(f'{i+1} Custo: {model.x[i]}')

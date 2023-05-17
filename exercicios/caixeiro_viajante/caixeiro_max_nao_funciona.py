n = 5
c = [[0,2,8,4,7],
     [1,0,3,6,5],
     [1,7,0,4,3],
     [1,8,4,0,5],
     [5,3,9,4,0]]

from pyomo.environ import *

model = ConcreteModel()
model.x = Var([i for i in range(n)],[j for j in range(n)], domain=Binary)
model.y = Var([i for i in range(n)], domain=Binary)

def objective(model):
    soma = 0
    for i in range(n):
        for j in range(n):
            if j == i: continue
            soma += model.x[i,j] * c[i][j]
    return soma

model.obj = Objective(rule=objective, sense=minimize)

model.con = ConstraintList()

model.con.add(sum(model.y[i] for i in range(n)) == n)

for i in range(n):
    model.con.add(sum(model.x[i,j] if j != i else 0 for j in range(n)) == 1)

for i in range(n):
    for j in range(n):
        model.con.add(model.y[j] <= model.x[i,j])

solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
for i in range(n):
    for j in range(n):
        if model.x[i,j]() == 0: continue
        print(f'Cidade {i + 1} é atendida pela cidade {j + 1}')
        # print(f'Cliente {i + 1}, -->, {j + 1}, :, {model.y[i,j]()}')
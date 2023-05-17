n = 5
c = [[999,2,8,4,7],
     [1,999,3,6,5],
     [1,7,999,4,3],
     [1,8,4,999,5],
     [5,3,9,4,999]]

from pyomo.environ import *

model = ConcreteModel()

model.x = Var([i for i in range(n)],[j for j in range(n)], domain=Binary)

model.u = Var([i for i in range(n)], domain=NonNegativeIntegers)

def objective(model):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += model.x[i,j] * c[i][j]
    return soma

model.obj = Objective(rule=objective, sense=minimize)

model.con = ConstraintList()

for i in range(n):
    model.con.add(sum(model.x[i,j] for j in range(n)) == 1)

for j in range(n):
    model.con.add(sum(model.x[i,j] for i in range(n)) == 1)

# for i in range(2,n):
#     for j in range(2,n):
#         if i==j: continue
#         model.con.add(model.u[i] - model.u[j] + (n*model.x[i,j]) <= n-1)

model.con.add(sum(model.x[i,j] for i in range(n) for j in range(n)) >= 1)

# for i in range(n):
#     model.con.add(0 <= model.u[i] <= n-1)

solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
for i in range(n):
    for j in range(n):
        if model.x[i,j]() == 0: continue
        print(f'Cidade {i + 1} é vai para {j + 1}')
        # print(f'Cliente {i + 1}, -->, {j + 1}, :, {model.y[i,j]()}')
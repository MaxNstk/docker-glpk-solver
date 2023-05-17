# Temos uma fábrica que produz n produtos
# Cada produto i tem:
#   um custo ci; um preço de venda pi;
#   um custo de tecido ti; um tempo de producao ti;
#   um custo de aluguel ai
# A fábrica tem um total de tecido T
# A fábrica tem um total de horas disponíveis H

from pyomo.environ import *

T = 160 
H = 150
n = 3

#
h = [3,2,6]
t = [4,3,4]
c = [6,4,8]
p = [12,8,15]
a = [200,150,100]

M = 100000

model = ConcreteModel()

model.x = Var([i for i in range(n)], domain=NonNegativeIntegers)
model.y = Var([i for i in range(n)], domain=Binary)

def obj_func(model):
    soma = 0
    for i in range(n):
        soma += model.x[i]*(p[i] - c[i]) - a[i]*model.y[i]
    return soma

model.obj = Objective(rule=obj_func, sense=minimize)

model.con = ConstraintList()

# custo de horas
model.con.add(sum(model.x[i]*h[i] for i in range(n)) <= H)
model.con.add(sum(model.x[i]*t[i] for i in range(n)) <= T)

for i in range(n):
    model.con.add(model.x[i]<=M*model.y[i])


# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()
for i in range(n):
    if model.x[i]() == 0: continue
    print(f'{i+1} Custo: {model.x[i]}')

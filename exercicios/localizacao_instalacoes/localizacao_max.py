# Problema
# Existem n cidades
# É possível instalar até K instalações
# custo de instalação em uma cidade j é: fj para todo j de 1..n
# custo para uma cidade i ser atendida por uma cidade j: cij
# Todos clientes devem ser atendidos por alguma instalação

n = 5 
K = 2
f = [15,13,12,14,12]
c = [[0,2,8,4,7],
     [1,0,3,6,5],
     [1,7,0,4,3],
     [1,8,4,0,5],
     [5,3,9,4,0]]

from pyomo.environ import *

model = ConcreteModel()

# variáveis do custo de instalação
model.x = Var([i for i in range(n)], domain=Binary)

# variáveis do custo de atendimento
model.y = Var([i for i in range(n)], [j for j in range(n)], domain=Binary)

def objective_function(model):
    installation_cost = 0
    attending_cost = 0
    for i in range(n):
        installation_cost += model.x[i] * f[i]
        for j in range(n):
            attending_cost += model.y[i,j] * c[i][j]
    return installation_cost + attending_cost

model.obj = Objective(rule=objective_function, sense=minimize)

model.cons = ConstraintList()

# respeitando o limite de instalações
model.cons.add(sum(model.x[i] for i in range(n)) <= K)

# todas cidades devem ser atendidas por somente uma fabrica
for i in range(n):
    model.cons.add(sum(model.y[i,j] for j in range(n)) == 1)

for i in range(n):
    soma = 0
    for j in range(n):
        soma += model.y[i,j]
    model.cons.add(soma == 1)

# Se a cidade i é atendida pela cidade j, a cidade j tem que ter fábrica
for i in range(n):
    for j in range(n):
        model.cons.add(model.y[i,j] <= model.x[j])

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
for i in range(n):
    for j in range(n):
        if model.y[i,j]() == 0: continue
        print(f'Cidade {i + 1} é atendida pela cidade {j + 1}')
        # print(f'Cliente {i + 1}, -->, {j + 1}, :, {model.y[i,j]()}')
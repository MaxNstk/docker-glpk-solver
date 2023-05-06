from pyomo.environ import *

# Temos um ladrão que carrega uma mochila com peso P
# ladrão entra em uma casa com n itens.
# Cada item n tem um peso p e um valor v
# Achar a melhor combinação de itens, que retornarão o maior valor, sem ultrapassar o peso

# Var de decição, xi = {0, 1} para todo i pertencente em n
#   0 = Não leva, 1 = leva

n = 5
p = [3,4,1,7,6]
v = [2,3,2,4,4]
P = 9

model = ConcreteModel()

# uma variável para cada elemento n
model.x = Var([i for i in range(n)], domain = Binary)


# função objetivo consiste no somatório de xi * vi, para todo elemento n
def objective_function(model):
    result = 0
    for i in range(n):
        result += model.x[i] * v[i]
    return result

model.obj = Objective(expr= sum(model.x[i]*v[i] for i in range(n)))
# model.obj = Objective(rule = objective_function)

# Restrições
model.cons = ConstraintList()

# a soma dos pesos não pode ser maior q a mochila
model.cons.add(expr= sum(model.x[i]*p[i] for i in range(n)) <= P)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
# for i in range(m):
#     for j in range(n):
#         print(i + 1, '-->', j + 1, ':', model.x[i,j]())

from pyomo.environ import *

# Temos um ladrão que carrega uma mochila com peso P
# ladrão entra em uma casa com n itens.
# Cada item n tem um peso p e um valor v
# Achar a melhor combinação de itens, que retornarão o maior valor, sem ultrapassar o peso

# Var de decição, xi = {0, 1} para todo i pertencente em n
#   0 = Não leva, 1 = leva

n = 20
v = [4, 5, 1, 2, 7, 8, 6, 4, 2, 3, 8, 6, 4, 5, 2, 1, 3, 6, 7, 9]
p = [5, 2, 1, 4, 8, 7, 9, 5, 4, 1, 6, 7, 4, 8, 9, 4, 3, 2, 6, 8]
P = 35

model = ConcreteModel()

# uma variável para cada elemento n

# model.x = Var(range(n), domain = Boolean)
model.x = Var([i for i in range(n)], domain = Binary)


# função objetivo consiste no somatório de xi * vi, para todo elemento n
def objective_function(model):
    result = 0
    for i in range(n):
        result += model.x[i] * v[i]
    return result

model.obj = Objective(expr= sum(model.x[i]*v[i] for i in range(n)), sense=maximize)
# model.obj = Objective(rule = objective_function)

# Restrições
model.cons = ConstraintList()

# a soma dos pesos não pode ser maior q a mochila
model.cons.add(expr= sum(model.x[i]*p[i] for i in range(n)) <= P)

# Solução
solver = SolverFactory('glpk')
solver.solve(model).write()

for i in range(n):
    print(model.x[i]())
print()
print(model.obj.expr())

# for i in range(n):
# print(i + 1, '-->', j + 1, ':', model.x[i,j]())

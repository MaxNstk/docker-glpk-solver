print('oqawdw')

from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)
model.x3 = Var(domain = NonNegativeReals)

while True:
    print

# Função objetivo
model.obj = Objective(expr = 0.32 * model.x1 + 0.25 * model.x2 + 0.05 * model.x3, sense = minimize)

# Restrições
model.con1 = Constraint(expr = model.x1 + model.x2 + model.x3 == 100)
model.con2 = Constraint(expr = 0.045 * model.x1 + 0.037 * model.x2 == 4)

# Solução
opt = SolverFactory('glpk')
opt.solve(model)
print('SOLUÇÃO ÓTIMA')
print('Cerveja A:', model.x1())
print('Cerveja B:', model.x2())
print('Água:', model.x3())
print('Custo:', model.obj())
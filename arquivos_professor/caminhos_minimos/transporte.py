

from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x11 = Var(domain = NonNegativeReals)
model.x12 = Var(domain = NonNegativeReals)
model.x13 = Var(domain = NonNegativeReals)
model.x21 = Var(domain = NonNegativeReals)
model.x22 = Var(domain = NonNegativeReals)
model.x23 = Var(domain = NonNegativeReals)
model.x31 = Var(domain = NonNegativeReals)
model.x32 = Var(domain = NonNegativeReals)
model.x33 = Var(domain = NonNegativeReals)

# Função objetivo
#model.obj = Objective(expr = 3 * model.x11 + 1 * model.x12 + 100 * model.x13 + 4 * model.x21 + 2 * model.x22 + 4 * model.x23 + 100 * model.x31 + 3 * model.x32 + 3 * model.x33, sense = minimize)
model.obj = Objective(expr = 3 * model.x11 + 1 * model.x12 + 4 * model.x21 + 2 * model.x22 + 4 * model.x23 + 3 * model.x32 + 3 * model.x33, sense = minimize)

# Restrições de estoque
model.con1 = Constraint(expr = model.x11 + model.x12 + model.x13 <= 5)
model.con2 = Constraint(expr = model.x21 + model.x22 + model.x23 <= 7)
model.con3 = Constraint(expr = model.x31 + model.x32 + model.x33 <= 3)

# Restrições de demanda
model.con4 = Constraint(expr = model.x11 + model.x21 + model.x31 == 7)
model.con5 = Constraint(expr = model.x12 + model.x22 + model.x32 == 3)
model.con6 = Constraint(expr = model.x13 + model.x23 + model.x33 == 5)

# Restrições de pares depósito x cliente
model.con7 = Constraint(expr = model.x13 == 0)
model.con8 = Constraint(expr = model.x31 == 0)

# Solução
opt = SolverFactory('glpk')
opt.solve(model).write()
print()
print('Custo total:', model.obj())
print('1 --> 1:', model.x11())
print('1 --> 2:', model.x12())
print('1 --> 3:', model.x13())
print('2 --> 1:', model.x21())
print('2 --> 2:', model.x22())
print('2 --> 3:', model.x23())
print('3 --> 1:', model.x31())
print('3 --> 2:', model.x32())
print('3 --> 3:', model.x33())
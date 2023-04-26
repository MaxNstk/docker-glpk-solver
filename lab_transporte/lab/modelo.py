from pyomo.environ import *
import instancia
import sys

semente = int(sys.argv[1])

def mostra_solucao(model):
    print()
    print(f'Instância (semente): {semente}')
    print('    ', end = '')
    for j in range(instancia.n):
        print(f' {j+1:5} ', end = '')
    print()
    print('  ' + '-' * (instancia.n * 7 + 1))
    
    for i in range(instancia.m):
        print(f'{i+1} | ', end = '')
        for j in range(instancia.n):
            print(f' {model.x[i,j]():5} ', end = '')
        print()
    print()
    print('Custo total:', model.obj())


def resolve():
    instancia.gera(semente)

    # Criação do modelo
    model = ConcreteModel()

    # Variáveis de decisão: para cada par depósito x cliente
    model.x = Var([i for i in range(instancia.m)], [j for j in range(instancia.n)], domain = NonNegativeReals)

    def objective_function(model):
        result = 0
        for i in range(instancia.m):
            for j in range(instancia.n):
                result += model.x[i,j] * instancia.custos[i][j]
        return result

    # Função objetivo
    #model.obj = Objective(expr = sum(model.x[i,j]*instancia.custos[i][j] for i in range(instancia.m) for j in range(instancia.n)))
    model.obj = Objective(rule = objective_function)

    # Restrições
    model.cons = ConstraintList()

    for i in range(instancia.m):
        model.cons.add(expr = sum(model.x[i,j] for j in range(instancia.n)) <= instancia.estoque[i])

    for j in range(instancia.n):
        model.cons.add(expr = sum(model.x[i,j] for i in range(instancia.m)) == instancia.demanda[j])

    # Solução
    solver = SolverFactory('glpk')
    #solver.solve(model).write()
    results = solver.solve(model)

    if results.solver.termination_condition == 'optimal':
        mostra_solucao(model)    
    else:
        #instancia.mostra()
        print('Solução ótima não encontrada!')
    

resolve()
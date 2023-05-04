""" 
    ij E A = arco (ij) do conjunto de arcos A
    Fij = fluxo no arco, se passou ou não por ele, 0 ou 1
    Cij = custo do arco 

    minimiza = somatório de Fij * Cij para todo ij

    Variáveris de decisão: todo fij
"""

# ia tentar por matriz de adjacencia mas não pensei como fazer nós valorados
# [
# #     1,2,3,4,5,6,7
#     1[0,0,0,0,0,0,0],
#     2[0,0,0,0,0,0,0],
#     3[0,0,0,0,0,0,0],
#     4[0,0,0,0,0,0,0],
#     5[0,0,0,0,0,0,0],
#     6[0,0,0,0,0,0,0],
#     7[0,0,0,0,0,0,0],
# ]

from pyomo.environ import *

model = ConcreteModel()

# for current_node, neighbors in nodes.items():
#     for from_node, cost in neighbors['N+1']:
#         model.x.


model.x = Var([i for i in range(m)], [j for j in range(n)], domain = NonNegativeReals)

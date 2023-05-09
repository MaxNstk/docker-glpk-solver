# #Problema:

# Uma empresa está buscando formar uma equipe de trabalho com um grupo diverso de funcionários, 
# a fim de maximizar a criatividade e o desempenho da equipe. A empresa tem 10 funcionários disponíveis para a equipe,
# cada um com habilidades e conhecimentos específicos. A empresa deseja que a equipe tenha no máximo 5
# funcionários do mesmo departamento e no máximo 3 funcionários com a mesma formação acadêmica.
# Cada funcionário tem uma pontuação de diversidade, que mede o quão diferente ele é dos outros funcionários 
# em termos de departamento e formação acadêmica. A pontuação de diversidade de um funcionário é calculada
# como a soma dos valores absolutos das diferenças entre seu departamento e a média dos departamentos dos outros funcionários,
# e entre sua formação acadêmica e a média das formações acadêmicas dos outros funcionários.

from pyomo import environ


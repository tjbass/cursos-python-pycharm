"""
PEP - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python
import this

[1] - Utilize Camel Case (a ideia de utilizar inicial maiúscula para nomes simles e compostos,
estes últimos que devem ser escritos sempre juntos) para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientífica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (Não use TAB);

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco;
- separar funções e definições de classe com duas linhas em branco.
- métodos dentro de uma classe devem ser separados com uma única linha em branco.

[5] Imports devem ser sempre em linhas separadas;
exemplo:

import sys
import os

#Não há problema em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários
# ou docstrings e antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções:

# Não faça:

funcao( algo[ 1 ], { outro: 2 })

# ou

algo (1)

# Faça:

funcao(algo[1], {outro: 2})

# ou

algo(1)

[7] - Termine sempre uma instrução com uma nova linha.
"""
# import this

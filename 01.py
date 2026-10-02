# Escreva um programa em Phython que peca as seguintes informacoes:
# - Idade (um numero inteiro)
# - Altura em centimetros (um numero inteiro)
# - Tem sutorizacao dos pais? (uma string: "sim" ou "nao")
# 
# O programa dve exibir "acesso liberado" se o visitante puder 
# andar no brinaquedo, ou "acesso negado." caso contrario.
# 
# Regra
# O visitante pode entrar se:
# - tiver idade maior ou igual a 12 E altura maior ou igual a 140 OU
# - se tiver autorizacao igual a "sim".

idade = float(input("qual sua idade?"))
altura = float(input("quantos centimetros você tem?"))
autorizacao = str(input("tem autorizacao?")).strip().lower()
permite = autorizacao in ["sim","s","SIM","Sim","S","tudo have"]


if idade >= 12 and altura >= 140 or permite:
    print(f"acesso legalmente liberado diante de suas condições")
else:
    print(f"acesso fora de cogitação")



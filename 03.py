# escreva um programa em python que receba as seguintes quatro 
# informações do usuário:
# - Renda mensal (um numero float)
# - Score de crédito (um inteiro de 0 a 1000)
# - possui bens como garantia? (uma string: "sim" ou "não")
# - tem historico de inadimplencia? (uma string: "sim" ou "não")
# 
# o emprestimo sera APROVADO se o cliente cumprir uma das duas regras
# abaixo: 
# regra 1: ter renda mensal maior ou igual a R$3.000,00
#          e score de credito maior ou igual a 600
#          e NÃO ter historico de inadimplencia.
# regra 2: independente de renda ou score,
#          se o cliente NÃO tiver historico de inadimplencia
#          e possuir bens como garantia, ele tambem é aprovado. 
# 
# se o cliente não se encaixa em nenhuma das duas regras,
# o emprestimo será REPROVADO

renda = float(input("qual sua renda mensal?"))
score = float(input("quanto você tem de score?"
"(entre 0 a 600, com numeros inteiros)"))
garantia = str(input("tem garantia?(sim ou não)"))
historico = str(input("tem historico de inadimplencia?(sim ou não)"))

if (renda >= 3.000 and score >= 600 and historico == "não") or (historico == "não" and garantia == "sim"):
    print(f"aprovado")
else:
    print(f"reprovado")




# Escreva un programa em Phythhon que pergunte três informações ao usuário:
# - É estudante? (uma string: "sim" ou "não")
# - Dia da semana? (uma string: "terça" ou "outro")
# -Tipo da sala? (uma string: "vip" ou "comum")
#
# O programa deve exibir "Desconto aplicado!" ou "Valor integral"
#
# Regra
# O cliente genha o desconto se for estudante ou for terça 
# E a sala for comum.

estudante = str(input("você é estudante? (sim ou não)"))
dia_da_semana = str(input("qual dia da semana é hoje?(terça ou outro)"))
sala = str(input("quer sala, vip ou comum?"))

if (estudante == "sim" or dia_da_semana == "terça") and (sala == "comum"):
    print(f"desconto deveras aceito")
else:
    print(f"pagamento integral")


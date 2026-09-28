# NOME: KAYLLER WENDEL PEREIRA DE MACEDO
# ESCOLA: SENAI
# CIDADE: LUZIÂNIA
# DATA: 15/09/2026

# --- GABARITO: DESAFIO DA TABUADA (AULÃO) ---

print("--- TABUADA INTELIGENTE ---")
# Captura o número digitado pelo usuário (lembre-se do int!)
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\n Tabuada do {numero}:")
print("---------------------")

# O range(1, 11) vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)


print("------------------")

# O range(1, 11) vai gerar os números de 1 até 10
# (o último número no range sempre é ignorado)
for adicao in range(1, 11):
    resultado = numero + adicao
    # CORREÇÃO AQUI: Trocado 'multiplicador' por 'adicao' no print
    print(numero, "+", adicao, "=", resultado)
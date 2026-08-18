#NOME: Kayller Wendel Pereira de macedo
#TURMA: 1°A Desenvolvimento de Sistema
#PROFESSOR: Rodrigo Vilela
#DATA: 18/08/2026

# --- LIVE CODE: Aula 01 - Tipos de Dados e Strings ---

#1. Trabalhando com Números (int e float)
# Explicar aos alunos a necessidades de converter o input de texto para números
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (ex: 1.75): "))

#2. Manipulação de Textos (Strings)
frase = input("Digite uma frase que você gosta: ")

print("\n--- ANALISANDO SEUS DADOS ---")
# Fazendo cálculos simples com os números
print("Sua idade daqui a 5 anos será:", idade+5)
print("Sua altura em centímetros é:", altura*100, "cm")

#3. Usando Métodos de String
#Explicar o que o .upper(), .lower() e o len() fazem
print("Sua frase toda em  MAIÚSCULAS:", frase.upper())
print("Sua frase toda em minúsculas:", frase.lower())
print("A frase digitada tem", len(frase), "caracteres (incluindo espaços).")
print("-------------------------")

# Programa de calculo de media de notas
#Autor: Seu nome

# Entrada 
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota: "))
# Pocessamento
media = (nota1 + nota2) / 2
# Saida
print(f"\nAluno: {nome}")
print(f"Media: {media: .2f}")

if media >= 6:
    print("Situacao: Aprovado")
else:
    print("Situacao: Reprovado")
    
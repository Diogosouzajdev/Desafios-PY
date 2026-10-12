import random

print("=== JOKENPÔ ===")

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
computador = random.choice(opcoes)

print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (
    (jogador == "pedra" and computador == "tesoura") or
    (jogador == "papel" and computador == "pedra") or
    (jogador == "tesoura" and computador == "papel")
):
    print("Você venceu!")
elif jogador in opcoes:
    print("O computador venceu!")
else:
    print("Opção inválida! Escolha Pedra, Papel ou Tesoura.") 

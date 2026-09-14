#perguntas para o cliente
valor_casa = float(input("Qual o valor da valor da casa R$ : "))
salario = float(input("digite o seu salário R$: "))
anos = int( input("Quantos anos para quitar: ")) 
#calculos
meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30
#aprovação de crédito
print (f"prestação mensal: R$ {prestacao:.2f}")
print(f"limite de 30% do salário R$: {limite:.2f}")

if prestacao <= limite:
    print("Empréstimo Aprovado")

else:
    print("Empréstimo Negado")
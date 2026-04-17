produtos = {
    'banana': 3.50,
    'maçã': 4.00,
    'laranja': 2.50,
    'uva': 5.00,
    'abacaxi': 7.00
}
compras = []

print("Lista de produtos disponíveis:\n")

for produto, preco in produtos.items():
    print(f"{produto.capitalize()} - R$ {preco:.2f}")

resp = 's'

# O programa deve solicitar ao usuário que digite o nome de um produto e perguntar se ele deseja continuar.
while resp == 's':
    compras.append(input('\nDigite o nome do produto: '))
    resp = input('Deseja continuar? (s/n) ')

print("\nSua lista de compras:")
# Exibe a lista de produtos digitados, numerada e com a primeira letra de cada produto em maiúscula.
for i in range(len(compras)):
    compras[i] = compras[i].capitalize()
    print(f"Produto {i+1}: {compras[i]} - R$ {float(produto[1][list(produto[0]).index(compras[i].lower())]):.2f}")

total = 0
# Calcula o valor total da compra.
for i in range(len(compras)):
    total += float(produto[1][list(produto[0]).index(compras[i].lower())])
print(f"\nValor total da compra: R$ {float(total):.2f}")
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


while True:
    produto = input('\nDigite o nome do produto: ').lower()

    if produto in produtos:
        compras.append(produto)
    else:
        print("Produto não encontrado. Tente novamente.")
        continue

    resp = input('Deseja continuar? (s/n) ').lower()
    if resp != 's':
        break

print("\nSua lista de compras: ")
total = 0

for i, item in enumerate(compras, start=1):
    preco = produtos[item]
    total += preco
    print(f"Produto {i}: {item.capitalize()} - R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")


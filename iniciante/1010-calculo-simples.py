c1, qtd1, v1 = input().split()
c2, qtd2, v2 = input().split()

# print(type(qtd1), type(qtd2), type(v1), type(v2))

qtd1, qtd2, v1, v2 = int(qtd1), int(qtd2), float(v1), float(v2)

# print(type(qtd1), type(qtd2), type(v1), type(v2))
# print(f"c1 = {c1}, qtd1 = {qtd1}, v1 = {v1}")
# print(f"c2 = {c2}, qtd2 = {qtd2}, v2 = {v2}")

result = qtd1 * v1 + qtd2 * v2

print(f"VALOR A PAGAR: R$ {result:.2f}")
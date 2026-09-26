codigo, quantidade = map(int, input().split())

precos = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

print(f"Total: R$ {precos[codigo] * quantidade:.2f}")
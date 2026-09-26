idade_dias = int(input())

anos =  idade_dias // 365
resto_ano = idade_dias % 365

meses = resto_ano // 30
dias = resto_ano % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
montante = int(round(float(input()) * 100))

cem = montante // 10000
resto_cem = montante % 10000

cinquenta = resto_cem // 5000
resto_cinquenta = resto_cem % 5000

vinte = resto_cinquenta // 2000
resto_vinte = resto_cinquenta % 2000

dez = resto_vinte // 1000
resto_dez = resto_vinte % 1000

cinco = resto_dez // 500
resto_cinco = resto_dez % 500

dois = resto_cinco // 200
resto_dois = resto_cinco % 200

um = resto_dois // 100
resto_um = resto_dois % 100

cinquenta_centavos = resto_um // 50
resto_cinquenta_centavos =  resto_um % 50

vinte_centavos = resto_cinquenta_centavos // 25
resto_vinte_centavos = resto_cinquenta_centavos % 25

dez_centavos = resto_vinte_centavos // 10
resto_dez_centavos = resto_vinte_centavos % 10

cinco_centavos = resto_dez_centavos // 5
resto_cinco_centavos = resto_dez_centavos % 5

um_centavo = resto_cinco_centavos // 1
resto_um_centavo = resto_cinco_centavos % 10.01

print("NOTAS:")
print(f"{int(cem)} nota(s) de R$ 100.00")
print(f"{int(cinquenta)} nota(s) de R$ 50.00")
print(f"{int(vinte)} nota(s) de R$ 20.00")
print(f"{int(dez)} nota(s) de R$ 10.00")
print(f"{int(cinco)} nota(s) de R$ 5.00")
print(f"{int(dois)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(um)} moeda(s) de R$ 1.00")
print(f"{int(cinquenta_centavos)} moeda(s) de R$ 0.50")
print(f"{int(vinte_centavos)} moeda(s) de R$ 0.25")
print(f"{int(dez_centavos)} moeda(s) de R$ 0.10")
print(f"{int(cinco_centavos)} moeda(s) de R$ 0.05")
print(f"{int(um_centavo)} moeda(s) de R$ 0.01")
A, B, C = map(int, input().split())

maior_AB = (A + B + abs(A - B)) // 2

maior_final = (maior_AB + C + abs(maior_AB - C)) //2

print(f"{maior_final} eh o maior")
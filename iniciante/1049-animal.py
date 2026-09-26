palavra_1 = input().strip().lower()
palavra_2 = input().strip().lower()
palavra_3 = input().strip().lower()

animais = {
    ('vertebrado', 'ave', 'carnivoro'): 'aguia',
    ('vertebrado', 'ave', 'onivoro'): 'pomba',
    ('vertebrado', 'mamifero', 'onivoro'): 'homem',
    ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
    ('invertebrado', 'inseto', 'hematofago'): 'pulga',
    ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
    ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro'): 'minhoca'
}
chave = (palavra_1, palavra_2, palavra_3)

if chave in animais:
    print(animais[chave])
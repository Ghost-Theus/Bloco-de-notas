r = True
notas = [""]
titulo = [""]

while r:
    print("\n Bem vindo ao Bloco de Notas!")

    print("O que você deseja fazer?\n(1) - Criar uma nova nota\n(2) - Visualizar nota existente\n(3) - Sair")
    a = int(input())

    if a == 1:
        print("Digite o título:")
        title = input()
        titulo.append(title)
        print("Digite a nota:")
        nota = input()
        notas.append(nota)

    if a == 2:
        print("Qual nota você quer ler?")
        for i in range(len(titulo)):
            print(f"{i} - {titulo[i]}")
        b = int(input())
        print("\n" + titulo[b])
        print("\n" + notas[b])

    if a == 3:
        r = False

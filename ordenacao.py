import os 
os.system("cls || clear")

def main():
    frutas = []

    while True:
        fruta = input("Digite o nome de uma fruta (ou 'sair' para encerrar): ").strip()
        if fruta.lower() == 'sair':
            break
        elif fruta:
            frutas.append(fruta)

    # Exibindo os resultados
    print("\nLista Original:")
    print(frutas)

    print("\nLista Ordenada:")
    print(sorted(frutas))

    print("\nLista na Ordem Inversa:")
    print(list(reversed(frutas)))

if __name__ == "__main__":
    main()


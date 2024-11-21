import os

# Função para limpar a tela
def limpar_tela():
    os.system("cls || clear")

# Função para ordenar a lista de frutas
def ordenar_lista(frutas):
    return sorted(frutas)

# Função para ordenar a lista de frutas na ordem inversa
def ordenar_inverso(frutas):
    return frutas[::-1]

# Função principal
def main():
    frutas = []
    
    # Loop para coleta das frutas
    while True:
        fruta = input("Digite o nome de uma fruta (ou 'sair' para encerrar): ").strip()
        
        # Condição de saída
        if fruta.lower() == 'sair':
            break
        elif fruta:
            frutas.append(fruta)
    
    # Exibindo os resultados
    exibir_resultados(frutas)

# Função para exibir as listas de frutas
def exibir_resultados(frutas):
    print("\nLista Original:")
    print(frutas)

    print("\nLista Ordenada:")
    print(ordenar_lista(frutas))

    print("\nLista na Ordem Inversa:")
    print(ordenar_inverso(frutas))

# Chama a função principal
if __name__ == "__main__":
    limpar_tela()
    main()

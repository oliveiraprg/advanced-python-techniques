# Usando funções interadoras como enumerate, zip, iter e next
def main():
    # Definindo lista dos dias em português e inglês
    dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    dias_en = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    # Função iter cria um interador sobre uma lista
    print('\nUsando next para fazer iteração na lista de dias')
    iterador_dias = iter(dias)
    print(next(iterador_dias))
    print(next(iterador_dias))
    print(next(iterador_dias))
   
    # Usando a função para iterar sobre um arquivo
    print('\nIterando sobre os dados de um arquivo')
    with open("cap02/dados.txt", "r", encoding="utf-8") as file_pointer:
        for linha in iter(file_pointer.readline, ''):
            print(linha)

    # Usando a iteração tradicional (range) sobre a lista dias
    print('\nPrint com range len')
    for numero in range(len(dias)):
        print(numero, dias[numero])

    # Usando a fução enumerate para iterar na lista
    print('\nPrint com enumerate')
    for i, dia in enumerate(dias):
        print(i, dia)

    # Usando função zip para parear valores em uma tupla 
    print('\nPareando dias em PT com os em EN')
    for d in zip(dias, dias_en):
        print(d)

    # Combinando zip com enumerate para formatar os dados
    for i, d in enumerate(zip(dias, dias_en)):
        print(i, d[0], ' = ', d[1], 'Em inglês')


if __name__ == "__main__":
    main()

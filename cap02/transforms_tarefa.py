# Usando funções transformadoras: sorted, filter, map
def primeiro_filtro(numero):
    if numero % 2 == 0:
        return False
    return True


def segundo_filtro(letra):
    if letra.isupper():
        return False
    return True


def quadrado(numero):
    return numero ** 2


def nota_para_conceito(nota):
    if nota >= 90:
        return "A"
    elif 80 <= nota < 90:
        return "B"
    elif 70 <= nota < 80:
        return "C"
    elif 65 <= nota < 70:
        return "D"
    else:
        return "F"


def main():
    numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letras = "abcDeFGHiJklmnoP"
    notas = (81, 89, 94, 78, 61, 66, 99, 74)
    
    # Usando filter para remover itens de uma lista
    print('\nFiltrando apenas os numeros impares')
    impares = list(filter(primeiro_filtro, numeros))
    print(impares)

    # Usando filter em uma sequência de caracteres    
    print('\nRetornando apenas as letras minusculas de uma string')
    minusculas = list(filter(segundo_filtro, letras))
    print(minusculas)

    # Usando map para criar uma nova sequencia de valores
    print('\nretornando os valores dos numeros ao quadrado')
    quadrados = list(map(quadrado, numeros))
    print(numeros)
    print(quadrados)

    # Usando sorted e map para mudar as notas para conceito
    print('\nOrdenando e aplicando conceitos sobre notas')
    notas = sorted(notas)
    conceitos = list(map(nota_para_conceito, notas))
    print(notas)
    print(conceitos)


if __name__ == "__main__":
    main()

# Iteradores do módulo itertools
import itertools


def condicao(x):
    return x < 40


def main():
    # iterando em uma lista com cycle
    print('\nFazendo iteração de uma lista com cycle e next')
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))

    # Usando count para criar um contador
    print('\nUsando count para criar um contador')
    contador = itertools.count(100, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))

    # Criando um iterador acumulador de valores com accumulate
    print('\nCriando um iterador acumulador de valores com accumulate')
    valores = [0, 2, 3, 50, 80, 13, 21, 4, 10, 200, 25]
    acumulado_max = itertools.accumulate(valores, max)
    acumulado = itertools.accumulate(valores)
    print(valores)
    print(list(acumulado))
    print(list(acumulado_max))

    # Usando a função chain para conectar listas
    print('\nUsando a função chain para conectar listas')
    corrente = itertools.chain("ABCD", "1234")
    print(list(corrente))

    # Usando dropwhile e takewhile para listar itens após condicional
    print('\nUsando dropwhile e takewhile para pegar itens após condicional')
    print('Caso a condição seja satisfeita, ele para de executar o comando.')
    print(valores, 'condicional 40')
    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))


if __name__ == "__main__":
    main()

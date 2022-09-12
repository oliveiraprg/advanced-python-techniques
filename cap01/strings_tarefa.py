# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = 'Isto é uma string'
    print(s)

    # Tentando concatenar os dois, retorna erro, comentando linha
    # print(s + b)

    # Forma cerda de unir bytes e strings com encoded e decod
    print(s + b.decode('utf-8'))
    print(s.encode('utf-32') + b)

if __name__ == '__main__':
    main()
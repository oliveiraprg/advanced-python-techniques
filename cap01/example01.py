# Mostrando o valor booleano em varios exemplos
lista = []
numero = 0
texto = ''
dicionario = {}
print(bool(lista), 'Lista')
print(bool(numero), ' Numero')
print(bool(texto), 'Texto')
print(bool(dicionario), 'Dicionario')

lista.append('Exemplo')

print(lista, bool(lista), ' Lista')
print(numero, bool(numero), ' Numero')
print(texto, bool(texto), 'Texto')
print(dicionario, bool(dicionario), 'Dicionario')
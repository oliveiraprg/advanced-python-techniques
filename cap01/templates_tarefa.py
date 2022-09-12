# Demonstração das funções de string templates
from string import Template

def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format(
        "Python Avançado", "Jessica Temporal")
    print(frase)
    # Criando um template com placeholders
    templ = Template("Você está assistindo ${curso} com ${instrutora}")
    # Passando o método substitute para substituir os parametros
    frase_2 = templ.substitute(
        curso="Python Avançado",
        instrutora="Jessica Temporal"
    )
    print(frase_2)
    # Usando método substitute com um dicionário
    dados = {
        "curso": "Python Avançado",
        "instrutora": "Jessica Temporal"
    }
    frase_3 = templ.substitute(dados)
    print(frase_3)

if __name__ == "__main__":
    main()

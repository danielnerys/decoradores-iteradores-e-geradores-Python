def principal():
    print('Executando função principal')

    def funcao_secundaria():
        print('Funcao secundaria')

    def funcao_terciaria():
        print('Função terceira')

    funcao_secundaria()
    funcao_terciaria()

# ambas funções abaixo estão dentro do escopo da função principal, por isso não podem ser acessadas fora do escopo dela.
# funcao_secundaria()
# funcao_terciaria()


# A função principal, quando é chamada, tras o retorno de suas funções internas
principal()

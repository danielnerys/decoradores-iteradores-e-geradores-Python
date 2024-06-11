def mensagem(funcao):
    def envelope():
        print("Inicando execução")
        funcao()
        print("Executou")
    return envelope

# utilizando o decorador @ na função mensagem para definir a funcao executando como seu parametro
@mensagem
def executando():
    print('Executando')


executando()

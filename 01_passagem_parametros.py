# arquivo de estudo de inner functions, funções que recebem outras funções como parametros
def mensagem(nome):
    print("Executando função mensagem")
    return f'Oi {nome}'


def mensagem_longa(nome):
    print('Executando função mensagem longa')
    return f'Oi {nome}, tudo bem com voce?'


def executar(funcao, nome):
    return print(funcao(nome))


executar(mensagem, 'daniel')

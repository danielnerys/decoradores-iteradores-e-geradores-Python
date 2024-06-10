def calculo(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def multi(a, b):
        return a * b

    def div(a, b):
        return a/b

    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return multi
        case '/':
            return div


def printar(funcao):
    print(funcao)


# Na função calculo, ele tem o parametro 'operacao' para receber o operador, que sera utilizado no match para retornar qual função será chamada.
printar(calculo('+')(2, 5))

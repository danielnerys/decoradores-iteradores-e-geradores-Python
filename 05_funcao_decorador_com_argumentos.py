def duplicar(func):
    def envelope(*args, **kwargs):
        print('Executando')
        resultado = func(*args, **kwargs)
        print('Executado')
        return resultado

    return envelope


@duplicar
def aprender(tecnologia):
    print(f'Eu estou aprendendo {tecnologia}')
    return tecnologia.upper()


resultado = aprender("Python")

print(resultado)

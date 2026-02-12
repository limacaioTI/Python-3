# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func): #def criar_funcao(inverte_string)
    def interna(*args, **kwargs): # Esses parâmetros são flexíveis, podendo ser passado de 0 a 10 parâmetros, diferentemente se fosse interna(a, b) 
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao # == inverte_string = criar_funcao(inverte_string)
def inverte_string(string): #Aponta para interna
    print(f'{inverte_string.__name__}') # == print = interna
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)
from operator import mod, eq

# função recebe numero inteiro e retorna uma string
def queijo(numero: int) -> str:
    return 'queijo' if eq(mod(numero, 3), 0) else numero

def queijo_goiabada(numero: int) -> str:
    return 'romeu e julieta' if eq(mod(numero, 3), 0) and eq(mod(numero, 5), 0 ) else numero

def goiabada(numero: int) -> str:
    return 'goiabada' if eq(mod(numero, 5), 0) else numero

def romeu_julieta(valorEntrada:int):
    if queijo_goiabada(valorEntrada) == 'romeu e julieta':
        return 'romeu e julieta'

    if queijo(valorEntrada) == 'queijo':
        return 'queijo'
    
    if goiabada (valorEntrada) == 'goiabada':
        return 'goiabada'


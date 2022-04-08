from operator import mod, eq
from typing import Callable, Any
from functools import wraps

# comopose recebe n funcoes
def compose(*funcs):
    # funcao interna que recebe argumento x
    def inner(arg):
        # estado recebe o argumento
        state = arg
        for func in reversed(funcs):
            # receba o estado da funcao anterior
            state = func(state)
        return state
    return inner

# decorador validar int
def is_int(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, int) else val

    return inner

@is_int
# função recebe numero inteiro e retorna uma string
def queijo(numero: int) -> str:
    return 'queijo' if eq(mod(numero, 3), 0) else numero


@is_int
def queijo_goiabada(numero: int) -> str:
    return 'romeu e julieta' if eq(mod(numero, 3), 0) and eq(mod(numero, 5), 0 ) else numero


@is_int
def goiabada(numero: int) -> str:
    return 'goiabada' if eq(mod(numero, 5), 0) else numero

# def romeu_julieta(valorEntrada:int):
#     if queijo_goiabada(valorEntrada) == 'romeu e julieta':
#         return 'romeu e julieta'

#     if queijo(valorEntrada) == 'queijo':
#         return 'queijo'
    
#     if goiabada (valorEntrada) == 'goiabada':
#         return 'goiabada'

romeu_julieta = compose(goiabada, queijo, queijo_goiabada)

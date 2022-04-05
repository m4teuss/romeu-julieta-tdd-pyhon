"""
Problema:
Uma entrada de valores numéricos (uma listas deles)

3x -> Queijo
5x -> Goiabada
3x e 5x -> Romeu e Julieta
"""

from unittest import TestCase, main
from app import romeu_julieta 

class TesteRomeuEJulieta(TestCase):
    #def teste_existe_romeu_e_julieta(self):
        #romeu_julieta()

    def teste_rej_deve_retornar_queijo_quando_input_for_3(self):
        """romeu_julieta (3) -> 'queijo'"""
        valor_entrada = 3
        valor_esperado = 'queijo'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)

    def teste_rej_deve_retornar_goiabada_quando_input_for_5(self):
        """romeu_julieta (3) -> 'queijo'"""
        valor_entrada = 5
        valor_esperado = 'goiabada'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)

    # multiplo de 3 ou 5
    def teste_rej_deve_retornar_romeu_e_julieta_quando_input_for_15(self):
        """romeu_julieta (3) -> 'queijo'"""
        valor_entrada = 15
        valor_esperado = 'romeu e julieta'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)

main()
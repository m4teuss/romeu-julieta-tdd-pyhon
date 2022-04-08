"""
Problema:
Uma entrada de valores numéricos (uma listas deles)

3x -> Queijo
5x -> Goiabada
3x e 5x -> Romeu e Julieta
"""

from unittest import TestCase, main
from app import romeu_julieta, romeus_julietas 

class TesteRomeuEJulieta(TestCase):
    #def teste_existe_romeu_e_julieta(self):
        #romeu_julieta()

    def teste_romeu_e_julieta_deve_retornar_queijo_quando_input_for_multiplos_de_3(self):
        """romeu_julieta (3) -> 'queijo'"""
        valores_entrada = [3, 6, 9]
        valor_esperado = 'queijo'
        for valor in valores_entrada:
            with self.subTest(valor = valor):
                self.assertEqual(romeu_julieta(valor), valor_esperado)

    def teste_romeu_e_julieta_deve_retornar_goiabada_quando_input_for_5(self):
        """romeu_julieta (3) -> 'queijo'"""
        valores_entrada = [5, 10, 20]
        valor_esperado = 'goiabada'
        for valor in valores_entrada:
            with self.subTest(valor = valor):   
                self.assertEqual(romeu_julieta(valor), valor_esperado)

    # multiplo de 3 ou 5
    def teste_romeu_e_julieta_deve_retornar_romeu_e_julieta_quando_input_for_15(self):
        """romeu_julieta (3) -> 'queijo'"""
        valor_entrada = 15
        valor_esperado = 'romeu e julieta'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)


    def teste_romeus_e_julietas_deve_retornar_queijo_goiabada_e_romeu_julieta_quando_receber_uma_lista_com_todos_os_multiplos(self):
        valores_entrada = [3, 5, 15]
        valor_esperado = ['queijo', 'goiabada', 'romeu e julieta']
        self.assertEqual(romeus_julietas(valores_entrada), valor_esperado)

main()
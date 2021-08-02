import pytest

from roller.dice import Dice, Roller
from roller.exceptions import InvalidOperation

'''
>>> dice = Dice(20)

>>> dice.roll()
18

>>> roller = Roller('1d20')

>>> roller.result
18

>>> roller = Roller('1d20 + 1d6 + 4')
>>> roller = Roller('1d20 + 1d8')

>>> 
'''


def test_se_instaciar_dado_sem_parametros_levanta_excecao():
    '''
    Testa se instanciar um Dice sem os parametros necessários
    levanta uma exceção TypeError.
    '''
    with pytest.raises(TypeError):
        Dice()


def test_instaciar_dado_com_parametros_necessarios():
    '''
    Testa se é instanciada a classe Dice com os parametros
    necessários e retorna um tipo Dice.
    '''
    dice = Dice(20)
    assert isinstance(dice, Dice)


def test_metodo_roll_retona_um_numero():
    dice = Dice(20)
    resultado = dice.roll()
    assert isinstance(resultado, int)


def test_metodo_roll_retorna_numero_dentro_do_range():
    dice = Dice(2)
    resultado = dice.roll()
    assert resultado > 0 and resultado <= dice.faces


def test_se_instaciar_roller_sem_parametros_levanta_excecao():
    '''
    Testa se instanciar um Roller sem os parametros necessários
    levanta uma exceção TypeError.
    '''
    with pytest.raises(TypeError):
        Roller()


def test_instaciar_roller_com_parametros_necessarios():
    '''
    Testa se é instanciada a classe Roller com os parametros
    necessários e retorna um tipo Roller.
    '''
    roller = Roller('1d20')
    assert isinstance(roller, Roller)


def test_roller_result_retona_int():
    roller = Roller('1d20')
    result = roller.result
    assert isinstance(result, int)


def test_metodo_result_para_operacao_complexa_com_soma_retorna_int():
    roller = Roller('1d20 + 3')
    result = roller.result
    assert isinstance(result, int)


def test_metodo_result_para_operacao_complexa_com_subtracao_retorna_int():
    roller = Roller('1d20 - 3')
    result = roller.result
    assert isinstance(result, int)


def test_metodo_result_para_operacao_complexa_com_subtracao_e_soma_retorna_int():
    roller = Roller('1d20 - 1d6 + 5')
    result = roller.result
    assert isinstance(result, int)


def test_metodo_result_para_operacao_invalida():
    with pytest.raises(InvalidOperation):
        roller = Roller('a')
        result = roller.result

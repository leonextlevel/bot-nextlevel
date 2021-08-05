from random import randint
from roller.exceptions import InvalidOperation


def somar(num_1, num_2):
    return num_1 + num_2


def subtrair(num_1, num_2):
    return num_1 - num_2


class Dice:
    def __init__(self, faces: int) -> None:
        self.faces = faces
    
    def roll(self):
        return randint(1, self.faces)


class Roller:
    OPERATORS = {
        '+': somar,
        '-': subtrair,
    }

    def __init__(self, operation: str, explosion=False) -> None:
        self.operation = operation
        self.explosion = explosion
        self.all_results = {}
        self.result = self._get_result()

    def _calculate(self, num_1, num_2, operator):
        return self.OPERATORS[operator](num_1, num_2)

    def _roll(self, faces, initial=None):
        if initial is None:
            initial = []
        resultados = initial
        rolagem = Dice(faces).roll()
        resultados.append(rolagem)
        if rolagem == faces:
            resultados.extend(self._roll(faces=faces, initial=resultados))
        return resultados

    def _transform_int(self, value):
        try:
            return int(value)
        except ValueError:
            try:
                amount = int(value.split('d')[0])
                faces = int(value.split('d')[1])
            except ValueError:
                raise InvalidOperation
            dice_results = []
            for _ in range(amount):
                dice_results.extend(self._roll(faces))
            self.all_results[value] = dice_results
            return sum(dice_results)

    def _tranform_operation(self):
        '''
        Transforma a operacao de infixa para posfixa.

        1 + 2 - 3
        1 2 + 3 -
        '''
        operations = self.operation.split()
        resultado = []
        aux = []
        for item in operations:
            if item not in self.OPERATORS.keys():
                resultado.append(item)
            elif not len(aux):
                aux.append(item)
            else:
                resultado.append(aux.pop())
                aux.append(item)
        if len(aux):
            resultado.append(aux.pop())
        return resultado

    def _get_result(self):
        operations = self._tranform_operation()
        pilha = []
        for item in operations:
            if item not in self.OPERATORS.keys():
                pilha.append(item)
            else:
                num_2 = self._transform_int(pilha.pop())
                num_1 = self._transform_int(pilha.pop())
                pilha.append(self._calculate(num_1, num_2, item))
        return self._transform_int(pilha.pop())
    
    def get_success_message(self):
        header = '> RESULTADO :game_die:\n'
        content = ''
        for dice, value in self.all_results.items():
            content += f'> {dice}: {value}\n'
        content += f'> **TOTAL:** {self.result}'
        return f'{header}{content}'

    @classmethod
    def get_error_message(cls):
        return (
            '> :robot: Pani no sistema!\n'
            '> Rolagem inválida :x:\n'
            '> Tente seguir o exemplo:\n'
            '> !roll 1d20 + 2'
        )

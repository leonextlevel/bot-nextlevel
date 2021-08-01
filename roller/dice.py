from random import randint


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

    def __init__(self, operation: str) -> None:
        self.operation = operation

    def _calculate(self, num_1, num_2, operator):
        return self.OPERATORS[operator](num_1, num_2)

    def _transform_int(self, value):
        try:
            return int(value)
        except ValueError:
            amount = int(value.split('d')[0])
            faces = int(value.split('d')[1])
            return sum([
                Dice(faces).roll() for _ in range(amount)
            ])

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

    @property
    def result(self):
        return self._get_result()

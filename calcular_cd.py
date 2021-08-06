'''
CD - Classe de Dificuldade

Valor do CD é a quantidade de rolagens de sucesso.

Fracasso = Rolagem de 1 a 5
Sucesso = Rolagem de  6 a 10
'''
from statistics import mean
from roller import Roller

for cd in range(1, 11):
    for qtd_dados in range(1, 11):
        lista_aux = []
        for _ in range(10):
            rolagens = [
                Roller(f'{qtd_dados}d10').results_list for _ in range(10000)
            ]
            def filtra_sucessos(elemento):
                lista_sucessos = list(filter(lambda x: x > 5, elemento))
                if len(lista_sucessos) >= cd:
                    return True
                return False

            lista_aux.append(len(list(filter(filtra_sucessos, rolagens))))
        media = mean(lista_aux) / 10000 * 100
        print(f'CD: {cd}   -   DADOS: {qtd_dados} ', "%.2f%%" % media)

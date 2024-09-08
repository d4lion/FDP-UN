from os import path

actual_path = path.dirname(path.abspath(__file__))

with open(f'{actual_path}/utils/discurso.txt') as file:
    lineas = file.readlines()
    file.close()

lineas_limpias = list(map(lambda x: x.replace('\n', '').strip(), lineas))

for texto in lineas_limpias:
    texto = texto.lower()

    opositivas = 0
    causativas = 0

    opositivas += texto.count('por otro lado')
    opositivas += texto.count('a pesar de')
    opositivas += texto.count('en cambio')
    opositivas += texto.count('mientras que')
    opositivas += texto.count('no solo')
    opositivas += texto.count('sin embargo')

    causativas += texto.count('hacer que')
    causativas += texto.count('obligar a')
    causativas += texto.count('convencer a')
    causativas += texto.count('inducir a')
    causativas += texto.count('permitir que')

    print(f'Opositivos: {opositivas} Causativos: {causativas}')

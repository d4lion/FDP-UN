from os import path

actual_path = path.dirname(path.abspath(__file__))

with open(f'{actual_path}/utils/trifilios.txt') as file:
    ls = file.readlines()

    ls_clean = list(map(lambda x: x.replace('\n', '').strip().split(' '), ls))

    print(ls_clean, file=open('output.txt', 'w'))

    for index, cadena in enumerate(ls_clean):
        cadena = cadena[0].split('-')

        palabra_1 = cadena[0]
        palabra_2 = cadena[1]

        # Caso 1: Tomando las 2 ultimas letras de la palabra
        if f'{palabra_1[-2:]}{palabra_1[:len(palabra_1) - 2]}' == palabra_2:
            print(
                f'{palabra_1[-2:]}{palabra_1[:len(palabra_1) - 2]} -> {palabra_2}')


[['monja-jamon'], ['gato-toga'], ['lava-bala'], ['el-le'], ['bronca-cabron'], ['amor-mora'], ['bolo-lobo'], ['bronca-cabron'], ['cala-laca'], ['cana-naca'], ['capa-paca'], ['carro-roca'], ['casa-saca'], ['colo-loco'], ['como-moco'], ['copa-paco'], ['cota-taco'], ['gama-maga'], ['cucala-lacuca'], ['gato-toga'], ['goma-mago'], ['jamon-monja'],
    ['lapa-pala'], ['lava-bala'], ['lomo-molo'], ['llama-malla'], ['llave-vella'], ['lleva-valle'], ['paso-sopa'], ['perra-rrape'], ['posa-sapo'], ['pata-tapa'], ['pato-topa'], ['peta-tape'], ['soto-toso'], ['adios-diosa'], ['labio-viola'], ['amaca-cama'], ['amarra-rama'], ['esela-lavese'], ['casese-seseca'], ['pasese-sesepa']]

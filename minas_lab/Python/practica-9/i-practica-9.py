def traducir_morse(palabras: str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '.': '.-.-.-', ',': '-.-.--'
    }

    palabras = palabras.upper().split(" ")

    palabra_morse = []

    for arr_palabra in palabras:
        palabra_traducida = " "

        for letra in arr_palabra:
            palabra_traducida += f" {morse_code_dict.get(letra)}"

        palabra_morse.append(palabra_traducida.strip())

    return " / ".join(palabra_morse)


cantidad_de_palabras = int(input())
traducciones = []

for i in range(cantidad_de_palabras):
    palabra = input()
    traducciones.append(traducir_morse(palabra))

for traduccion in traducciones:
    print(f"{traduccion}\n")

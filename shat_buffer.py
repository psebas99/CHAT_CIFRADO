from code_cesar import cesar_code
from code_hill import hill_code
from code_vigenere import vig_code
from code_hamming import hamming
from decode_cesar import cesar_decode
from decode_hill import hill_decode
from decode_vigenere import vigenere_decode
from decode_hamming import deco_hamming
from envio import enviar
from recepcion import recibir
from langdetect import detect

tx = False
rx = False

print("---->CHAT GRUPO 6<----\n¿Qué desea hacer?")
print("1. Enviar un mensaje")
print("2. Recibir un mensaje")
opcion = input("Acción a realizar:")
op = int(opcion)
choose_cifrado = choose_decodificado = False
leer_cesar = leer_hill = leer_vigenere = False
if op == 1:
    tx = True
    rx = False
    choose_cifrado = True
elif op == 2:
    tx = False
    rx = True
    choose_decodificado = True
while True:
    while choose_cifrado and tx:
        cifrado = int(input("\n¡CIFREMOS!\nINGRESE CIFRADO:\n[1] CESAR\n[2] HILL\n[3] VIGENERE\n... : "))
        if cifrado == 1:
            enviar(hamming(cesar_code("hola ordenador vamos a cifrar en cesar")))
        elif cifrado == 2:
            enviar(hamming(hill_code("hola ordenador vamos a cifrar en hill")))
        elif cifrado == 3:
            enviar(hamming(vig_code("hola ordenador vamos a cifrar en vigenere")))
        choose_cifrado = False

    while tx:
        if cifrado == 1:
            mensaje = input("TÚ: ")
            enviar(hamming(cesar_code(mensaje)))
            leer_cesar = True
            leer_hill = leer_vigenere = False

        elif cifrado == 2:
            mensaje = input("TÚ: ")
            enviar(hamming(hill_code(mensaje)))
            leer_hill = True
            leer_vigenere = leer_cesar = False

        elif cifrado == 3:
            mensaje = input("TÚ: ")
            enviar(hamming(vig_code(mensaje)))
            leer_vigenere = True
            leer_cesar = leer_hill = False

        tx = False
        rx = True

    while choose_decodificado and rx:
        print("\n¡DESCIFREMOS!")
        while True:
            try:
                mensaje = recibir()
                break
            except Exception:
                pass
        decodificado = deco_hamming(mensaje)
        decodificado_cesar = cesar_decode(decodificado)
        decodificado_hill = hill_decode(decodificado)
        decodificado_vigenere = vigenere_decode(decodificado)
        lang_cesar = lang_hill = lang_vigenere = None
        try:
            lang_cesar = detect(decodificado_cesar)
            lang_hill = detect(decodificado_hill)
            lang_vigenere = detect(decodificado_vigenere)
        except Exception:
            pass
        if lang_cesar == "es":
            leer_cesar = True
            leer_hill = leer_vigenere = False
            cifrado = 1
        elif lang_hill == "es":
            leer_hill = True
            leer_vigenere = leer_cesar = False
            cifrado = 2
        elif lang_vigenere == "es":
            leer_vigenere = True
            leer_cesar = leer_hill = False
            cifrado = 3

        choose_decodificado = False

    while rx:
        while True:
            try:
                mensaje = recibir()
                break
            except Exception:
                pass
        if leer_cesar:
            decodificado = deco_hamming(mensaje)
            decodificado_cesar = cesar_decode(decodificado)
            print(decodificado_cesar)
        elif leer_hill:
            decodificado = deco_hamming(mensaje)
            decodificado_hill = hill_decode(decodificado)
            print(decodificado_hill)
        elif leer_vigenere:
            decodificado = deco_hamming(mensaje)
            decodificado_vigenere = vigenere_decode(decodificado)
            print(decodificado_vigenere)
        tx = True
        rx = False
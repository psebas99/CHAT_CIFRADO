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

logico = False
while (not logico):

    print("\n¿Qué desea hacer?")
    print("1. Enviar un mensaje")
    print("2. Recibir un mensaje")
    opcion = input("Acción a realizar:")
    op = int(opcion)

    if op == 1:
        print("\n¡CIFREMOS!\n")
        print("Ingrese que cifrado quiere")
        print("1. Cifrado cesar")
        print("2. Cifrado hill")
        print("3. Cifrado vigenere")
        opcion1 = input("Ingrese su opcion:")
        op1 = int(opcion1)

        if op1 == 1:
            mensaje = input("Ingrese su mensaje a enviar:")
            codificado = cesar_code(mensaje)
            codificado1 = hamming(codificado)
            enviar(codificado1)
            print(codificado1)

        if op1 == 2:
            mensaje = input("Ingrese su mensaje a enviar:")
            codificado = hill_code(mensaje)
            codificado1 = hamming(codificado)
            enviar(codificado1)
            print(codificado1)

        if op1 == 3:
            mensaje = input("Ingrese su mensaje a enviar:")
            codificado = vig_code(mensaje)
            codificado1 = hamming(codificado)
            enviar(codificado1)
            print(codificado1)

    if op == 2:
        print("\n¡DESCIFREMOS!")
        mensaje = recibir()
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

        print("\n¡¡¡Mensaje codificado recibido!!!")
        print("Determinando tipo de cifrado...")
        if lang_cesar == "es":
            print("\nMensaje cifrado en Cesar:")
            print(decodificado_cesar)
        elif lang_hill == "es":
            print("\nMensaje cifrado en Hill:")
            print(decodificado_hill)
        elif lang_vigenere == "es":
            print("\nMensaje cifrado en Vigenere:")
            print(decodificado_vigenere)
        else:
            print("\nOracion ambigua")
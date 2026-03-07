import random
import string
import time


def evolucionar_con_conteo_total(frase_objetivo):
    objetivo = frase_objetivo.upper()
    # números y signos de puntuación porque tu frase los tiene
    caracteres_posibles = string.ascii_uppercase + string.digits + string.punctuation + " "

    # Estado inicial
    intento_actual = "".join(random.choice(caracteres_posibles) for _ in range(len(objetivo)))

    generaciones = 0
    intentos_de_letras = 0  # Este contará cada vez que el "mono" pulsó una tecla
    inicio_total = time.time()

    print(f"\n--- INICIANDO EVOLUCIÓN ---")

    while intento_actual != objetivo:
        generaciones += 1
        nueva_cadena = list(intento_actual)

        for i in range(len(objetivo)):
            if nueva_cadena[i] != objetivo[i]:
                # Aquí es donde ocurre el "intento"
                nueva_cadena[i] = random.choice(caracteres_posibles)
                intentos_de_letras += 1  # Sumamos un intento individual

        intento_actual = "".join(nueva_cadena)

        # Imprimimos cada 20 generaciones para no frenar la PC con tanto texto
        if generaciones % 20 == 0:
            print(f"Gen {generaciones:04d} | Intentos acumulados: {intentos_de_letras:,}")

    fin_total = time.time()
    tiempo_total = fin_total - inicio_total

    print("\n" + "=" * 50)
    print(f"📊 REPORTE DE EVOLUCIÓN")
    print(f"Frase: {intento_actual[:50]}...")
    print(f"Generaciones (revisiones): {generaciones}")
    print(f"Intentos individuales de letras: {intentos_de_letras:,}")
    print(f"Tiempo de cómputo: {tiempo_total:.4f} segundos")
    print("=" * 50)



frase = "Prueba"

evolucionar_con_conteo_total(frase)

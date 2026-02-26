from PIL import Image
import random
import os
import time

def evolucionar_imagen_inteligente(nombre_archivo_entrada):
    # 1. Cargar y REDIMENSIONAR automáticamente a 50x50 para velocidad
    try:
        img_original = Image.open(nombre_archivo_entrada).convert('RGB')
        img_original = img_original.resize((50, 50)) 
        ancho, alto = img_original.size
        pixels_objetivo = img_original.load()
        print(f" Imagen objetivo cargada: {ancho}x{alto} píxeles.")
    except Exception as e:
        print(f" Error al abrir la imagen: {e}")
        return

    # 2. Crear el lienzo inicial (puedes empezar en negro o ruido)
    img_actual = Image.new('RGB', (ancho, alto), (0, 0, 0)) # Empezamos en negro
    pixels_actual = img_actual.load()
    
    generacion = 0
    inicio_tiempo = time.time()
    total_pixeles = ancho * alto

    print(" Iniciando evolución inteligente...")
    print("Verás cómo la imagen 'emerge' de la oscuridad.")

    while True:
        generacion += 1
        pixeles_terminados = 0
        
        for x in range(ancho):
            for y in range(alto):
                r_obj, g_obj, b_obj = pixels_objetivo[x, y]
                r_act, g_act, b_act = pixels_actual[x, y]

                # Si el píxel ya es igual al objetivo, lo contamos como terminado
                if (r_act, g_act, b_act) == (r_obj, g_obj, b_obj):
                    pixeles_terminados += 1
                else:
                    # MUTACIÓN POR PROXIMIDAD:
                    # Acercamos cada canal (R, G, B) un paso hacia el objetivo
                    nuevo_r = r_act + (1 if r_obj > r_act else -1 if r_obj < r_act else 0)
                    nuevo_g = g_act + (1 if g_obj > g_act else -1 if g_obj < g_act else 0)
                    nuevo_b = b_act + (1 if b_obj > b_act else -1 if b_obj < b_act else 0)
                    
                    pixels_actual[x, y] = (nuevo_r, nuevo_g, nuevo_b)
        
        # Mostrar progreso cada 10 generaciones
        if generacion % 10 == 0 or pixeles_terminados == total_pixeles:
            porcentaje = (pixeles_terminados / total_pixeles) * 100
            print(f"Gen {generacion:03d} | Progreso: {pixeles_terminados}/{total_pixeles} píxeles ({porcentaje:.2f}%)")
            img_actual.save("progreso_evolucion.png")

        # Condición de victoria
        if pixeles_terminados == total_pixeles:
            break

    fin_tiempo = time.time()
    img_actual.save("resultado_final.png")
    print(f"\n ¡EVOLUCIÓN COMPLETADA! ")
    print(f"Generaciones: {generacion}")
    print(f"Tiempo total: {fin_tiempo - inicio_tiempo:.2f} segundos")
    print(f"Busca 'resultado_final.png' en tu carpeta.")

# --- EJECUCIÓN ---
archivo = "objetivo.jpg" 

if os.path.exists(archivo):
    evolucionar_imagen_inteligente(archivo)
else:
    print(f" No encontré '{archivo}'. Pon una imagen con ese nombre en la carpeta.")
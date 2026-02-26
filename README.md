🌀 Chaos Evolver: Del Azar a la Realidad
Este proyecto es una exploración práctica del Teorema de los Monos Infinitos. Utiliza algoritmos de búsqueda heurística y evolución para demostrar cómo el azar, cuando es guiado por un objetivo, puede crear orden a partir del caos absoluto.

🚀 ¿De qué trata?
¿Puede un grupo de monos escribiendo al azar en una máquina de escribir producir las obras de Shakespeare? Matemáticamente sí, pero tardarían eones. Este proyecto acelera ese proceso mediante Algoritmos Evolutivos.

El repositorio contiene dos experimentos principales:

Text Evolution: Un motor que genera frases complejas (desde una palabra hasta biografías completas) adivinando letra por letra y conservando los aciertos.

RGB Pixel Mutation: Un script que recrea imágenes píxel por píxel. Empieza con "estática" de televisor y termina materializando una imagen clara (como una cafetera) mediante gradientes de color.

🧠 El Concepto: "El Escultor Ciego"
Imagina un escultor que no puede ver. Da golpes al azar a una piedra. Cada vez que un golpe acerca la piedra a la forma de una cafetera real, nosotros le decimos "¡Caliente!". Él conserva ese cambio y sigue golpeando.

Este software hace exactamente eso:

Generación Aleatoria: Empieza desde el desorden total.

Función de Aptitud (Fitness): Compara el resultado actual con el objetivo.

Selección: Mantiene lo que funciona y muta lo que no.

🛠️ Tecnologías utilizadas
Python 3.x

Pillow (PIL): Para la manipulación de imágenes y canales RGB.

Random & Time: Para la lógica de mutación y medición de rendimiento.

📊 Resultados impactantes
Texto: Capaz de resolver párrafos de más de 1,000 caracteres en milisegundos.

Imagen: Capaz de recrear una matriz de 2,500 píxeles (50x50) en menos de 255 pasos evolutivos utilizando optimización de gradiente.

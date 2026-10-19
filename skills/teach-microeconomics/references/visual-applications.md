# Gráficos y aplicaciones docentes

## Estándar visual obligatorio

Cuando un gráfico aporte comprensión, producirlo con Python, Seaborn y Matplotlib si hay ejecución disponible. Cargar `scripts/econ_style.py`: fondo blanco, cuadrícula tenue, tipografía DejaVu Sans, títulos legibles, líneas de 2.5 puntos, PNG de 200 dpi y SVG vectorial. Mantener colores consistentes entre escenarios y complementar con línea continua/discontinua, símbolos y etiquetas; no depender solo del color.

| Papel | HEX | RGB |
|---|---|---|
| Base | #0072B2 | 0, 114, 178 |
| Escenario alternativo | #D55E00 | 213, 94, 0 |
| Mecanismo complementario | #009E73 | 0, 158, 115 |
| Área destacada | #CC79A7 | 204, 121, 167 |
| Referencia neutral | #52606D | 82, 96, 109 |

No usar 3D decorativo, arcoíris, doble eje sin justificación ni escalas truncadas que alteren el mensaje. Mantener escalas iguales al comparar paneles. Etiquetar ejes, unidades, horizonte, supuestos y procedencia. Las áreas de recaudación no son automáticamente ganancias sociales ni los colores significan juicios normativos.

## Ejecutar y adaptar

Desde la carpeta de la skill:

```bash
python -m pip install -r scripts/requirements.txt
python scripts/plot_applications.py --out figures
```

Versiones verificadas: NumPy 2.3.5, Matplotlib 3.10.8, Seaborn 0.13.2. El script genera aplicaciones hipotéticas deterministas, cada una con PNG, SVG y JSON de parámetros/resultados. Revisar el código y modificar supuestos para adaptar al ejercicio; no presentar los casos fijos como motor general para cualquier dato.

Antes de entregar: ejecutar, comprobar restricciones y resultados analíticos, abrir imágenes e inspeccionar texto, leyendas, cruces y sombreados. Corregir solapamientos. Entregar gráfico y breve lectura económica; adjuntar código y parámetros cuando el usuario solicite reproducibilidad. Si no hay ejecución, facilitar código listo para correr y declarar que no se ejecutó; no simular una imagen obtenida.

## Secuencia para enseñar con un gráfico

1. En tutoría, pedir una predicción sobre una curva o escenario antes de mostrar la solución; en explicación completa, mostrar y explicar directamente.
2. Orientar la lectura: qué representa cada eje, variable fija y curva.
3. Explicar un cambio a la vez y señalar el punto o área que sostiene la conclusión.
4. Conectar gráfico, ecuación y ejemplo numérico; distinguir equilibrio de transición y representación conceptual de evidencia observada.
5. Cambiar un supuesto y pedir anticipar qué parte del gráfico se modifica y por qué. No confundir interpretación visual con demostración causal.

## Aplicaciones disponibles y extensiones

En macroeconomía: Solow compara inversión y reposición y grafica consumo estacionario frente al ahorro; deuda compara tres saldos primarios con la identidad exacta. Preguntar por regla de oro frente a bienestar intertemporal y por qué crecimiento o tasas endógenos cambian el escenario.

En microeconomía: impuesto muestra precios comprador/vendedor, recaudo y pérdida de eficiencia bajo ausencia de externalidades; consumidor compara restricciones y óptimos Cobb-Douglas con un aumento de precio. Preguntar cómo cambia el bienestar con una externalidad y por qué la variación ordinaria de demanda no es la demanda compensada.

Para nuevas aplicaciones —IS/Phillips, elasticidades, Cournot, riesgo, salarios o contratos— formular primero el modelo, validar sus resultados y adaptar el mismo tema visual; no presentar estas extensiones como scripts ya implementados. Para datos reales conservar fuente, fecha, transformaciones e incertidumbre; no agregar bandas estadísticas a simulaciones deterministas sin un modelo que las justifique.

Documentación técnica consultada: https://seaborn.pydata.org/generated/seaborn.set_theme.html y https://seaborn.pydata.org/tutorial/color_palettes.html

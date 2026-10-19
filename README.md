# Structured Tools IA

Skills reutilizables para trabajo riguroso con asistentes de IA.

## Macroeconomía: aprender y analizar

La skill [`teach-macroeconomics`](skills/teach-macroeconomics/SKILL.md) combina enseñanza paso a paso, modelos, ejercicios y análisis sustentado en libros. Incluye una ruta desde fundamentos hasta posgrado, bibliografía temática y reglas para separar teoría, evidencia y escenarios.

### Usar con ChatGPT y Claude

El núcleo es Markdown portable, no depende de un proveedor ni requiere API. Publicar los archivos aquí no instala automáticamente la skill en ninguna cuenta.

- **Entorno compatible con skills:** incorporar la carpeta de la skill elegida (`skills/teach-macroeconomics` o `skills/teach-microeconomics`) siguiendo el mecanismo de skills de ese entorno. El punto de entrada es `SKILL.md`; conservar `references/` junto a él. `agents/openai.yaml` aporta metadatos opcionales para entornos compatibles con OpenAI.
- **ChatGPT o Claude mediante un proyecto/configuración de asistente:** incorporar las instrucciones de `SKILL.md` y adjuntar las referencias como contexto. Si el entorno no resuelve rutas relativas, adjuntar los archivos y referirse a sus nombres. Ajustar al mecanismo y límites de la interfaz disponible.
- **Conversación sin configuración persistente:** adjuntar `SKILL.md` y las referencias y solicitar que se sigan durante esa conversación. Esto no equivale a una instalación persistente.

No se incluyen libros completos. Para analizar un pasaje específico, aportar una copia o fragmento autorizado y su edición. La skill prohíbe inventar citas y páginas.

### Ejemplos

> Usa teach-macroeconomics para enseñarme la transmisión monetaria: intuición, ecuaciones, ejemplo y ejercicio. Fundamenta la explicación en libros e indica qué referencias puedes verificar.

> Explícame Solow a nivel de posgrado y ayúdame a derivar el estado estacionario antes de interpretar los resultados.

> Analiza la inflación colombiana con datos oficiales a una fecha de corte explícita. Separa datos, mecanismos teóricos y escenarios; explica qué evidencia falta.

> Construye una ruta de estudio de macroeconomía abierta y evalúa mi comprensión con ejercicios progresivos.

## Microeconomía: aprender y analizar

La skill [`teach-microeconomics`](skills/teach-microeconomics/SKILL.md) enseña consumidor, productor, dualidad, equilibrio, bienestar, organización industrial, juegos, incertidumbre, información y contratos. Incluye bibliografía temática, ruta de estudio y casos resueltos con controles para esquinas, incentivos y causalidad.

Aplicar las instrucciones de uso con ChatGPT y Claude indicadas arriba, utilizando esta carpeta y sus referencias. No requiere API ni incluye libros completos.

> Usa teach-microeconomics para enseñarme dualidad y la ecuación de Slutsky: intuición, derivación, ejemplo y ejercicio. Distingue lectura sugerida de pasajes verificados.

> Explícame la incidencia de un impuesto y ayúdame a resolver el equilibrio antes de calcular el bienestar.

> Compara Cournot y Bertrand con supuestos explícitos y muéstrame cuándo cambian las conclusiones.

## Método de estudio crítico

Ambas skills incluyen un seminario de razonamiento y talleres por disciplina. En tutoría, el estudiante formula una predicción, explicita supuestos, desarrolla el modelo, construye contraejemplos, contrasta mecanismos rivales y revisa su conclusión. La retroalimentación identifica la brecha concreta y ofrece ayudas graduadas. Si se solicita una solución completa, se entrega sin bloquearla con preguntas.

Los talleres de macroeconomía trabajan ahorro y bienestar, inflación e identificación, deuda, depreciación y distribución. Los de microeconomía trabajan Slutsky y Giffen, impuestos con externalidades, Bertrand/Cournot, eficiencia y equidad, seguros e información y contrastación de racionalidad.

> Trabaja en modo tutoría. Quiero defender la afirmación «una depreciación siempre estimula el PIB». Pídeme una predicción razonada y cuestiona mis supuestos, una pregunta por turno; ayúdame a construir un contraejemplo y revisar mi conclusión.

> Enséñame incidencia tributaria mediante un debate: primero un mercado competitivo y luego una externalidad. Hazme justificar qué cambia en el juicio de bienestar y qué evidencia necesitaría para recomendar la política.

## Aplicaciones visuales con Python y Seaborn

Ambas skills incorporan un tema visual consistente, colores distinguibles, ejemplos numéricos y exportación PNG/SVG con parámetros JSON. Aplicaciones ejecutables: **Solow y consumo**, **trayectorias de deuda**, **incidencia tributaria** y **elección del consumidor**. Consultar `references/visual-applications.md` en cada skill para ejecución y uso docente. Los ejemplos son hipotéticos; no son datos actuales ni estimaciones empíricas.

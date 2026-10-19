# Structured Tools IA

Skills reutilizables para trabajo riguroso con asistentes de IA.

## Macroeconomía: aprender y analizar

La skill [`teach-macroeconomics`](skills/teach-macroeconomics/SKILL.md) combina enseñanza paso a paso, modelos, ejercicios y análisis sustentado en libros. Incluye una ruta desde fundamentos hasta posgrado, bibliografía temática y reglas para separar teoría, evidencia y escenarios.

### Usar con ChatGPT y Claude

El núcleo es Markdown portable, no depende de un proveedor ni requiere API. Publicar los archivos aquí no instala automáticamente la skill en ninguna cuenta.

- **Entorno compatible con skills:** incorporar la carpeta `skills/teach-macroeconomics` siguiendo el mecanismo de skills de ese entorno. El punto de entrada es `SKILL.md`; conservar `references/` junto a él. `agents/openai.yaml` aporta metadatos opcionales para entornos compatibles con OpenAI.
- **ChatGPT o Claude mediante un proyecto/configuración de asistente:** incorporar las instrucciones de `SKILL.md` y adjuntar las cuatro referencias como contexto. Si el entorno no resuelve rutas relativas, adjuntar los archivos y referirse a sus nombres. Ajustar al mecanismo y límites de la interfaz disponible.
- **Conversación sin configuración persistente:** adjuntar `SKILL.md` y las referencias y solicitar que se sigan durante esa conversación. Esto no equivale a una instalación persistente.

No se incluyen libros completos. Para analizar un pasaje específico, aportar una copia o fragmento autorizado y su edición. La skill prohíbe inventar citas y páginas.

### Ejemplos

> Usa teach-macroeconomics para enseñarme la transmisión monetaria: intuición, ecuaciones, ejemplo y ejercicio. Fundamenta la explicación en libros e indica qué referencias puedes verificar.

> Explícame Solow a nivel de posgrado y ayúdame a derivar el estado estacionario antes de interpretar los resultados.

> Analiza la inflación colombiana con datos oficiales a una fecha de corte explícita. Separa datos, mecanismos teóricos y escenarios; explica qué evidencia falta.

> Construye una ruta de estudio de macroeconomía abierta y evalúa mi comprensión con ejercicios progresivos.

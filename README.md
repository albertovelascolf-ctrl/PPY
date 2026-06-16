# PPY — Python para Principiantes

Repositorio de materiales para repasar los conceptos fundamentales de Python desde cero. Hay desde teoría en notebooks a archivos .py con ejercicios dentro para poder repasar. Acuerdate de mirar el documento asociado en classroom para mejor entendimiento.

## Estructura del repositorio

```
PPY/
├── teoria/       → Notebooks de Jupyter con explicaciones teóricas y ejemplos
└── repaso/       → Archivos .py con ejercicios para practicar
```

## Contenido

### teoria/ — Notebooks de Jupyter

Cada notebook explica un tema con teoría detallada y ejemplos ejecutables paso a paso.

| Notebook | Tema |
|---|---|
| `00_TUTORIAL.ipynb` | Pequeña introducción al entorno |
| `01_INTRODUCCIÓN_A_LA_PROGRAMACIÓN.ipynb` | Conceptos básicos y operadores |
| `02_ESTRUCTURAS_DE_CONTROL.ipynb` | if / elif / else, operadores lógicos, for, while, range, break, continue |
| `03_ESTRUCTURA_DE_DATOS.ipynb` | Listas, diccionarios y sus métodos |
| `05_FUNCIONESipynb` |  Definición, parámetros, return, lambda |
| `05_CLASES.ipynb` | Clases, objetos, herencia |

### repaso/ — Archivos de ejercicios

Archivos `.py` con ejercicios al final para que el alumno practique cada tema.

| Archivo | Tema |
|---|---|
| `01_tipos_de_variables.py` | int, float, str, bool, None y conversiones |
| `02_manejo_de_strings.py` | Concatenación, f-strings, métodos, slicing |
| `03_estructuras_de_control.py` | if / elif / else, operadores lógicos |
| `04_bucles.py` | for, while, range, break, continue |
| `05_listas_y_diccionarios.py` | Listas, diccionarios y sus métodos |
| `06_funciones.py` | Definición, parámetros, return, lambda |
| `07_programacion_orientada_a_objetos.py` | Clases, objetos, herencia |

## Cómo descargar el repositorio

### Opción A — Descarga directa (sin instalar nada)

La forma más sencilla, sin necesidad de saber usar Git:

1. Haz clic en el botón verde **`<> Code`** que hay arriba en esta página
2. Selecciona **"Download ZIP"**
3. Descomprime el archivo ZIP en tu ordenador
4. ¡Listo! Ya tienes todos los archivos en tu carpeta

![Descarga ZIP](https://docs.github.com/assets/cb-60499/mw-1440/images/help/repository/code-button.webp)

### Opción B — Con Git (recomendado si ya lo tienes instalado)

```bash
git clone https://github.com/albertovelascolf-ctrl/PPY.git
cd PPY
```

---

## Cómo usar este repositorio

1. Descarga o clona el repositorio
2. Abre la carpeta en VSCode
3. **Empieza por `teoria/`**: abre el notebook del tema y lee los ejemplos
4. **Pasa a `repaso/`**: abre el `.py` correspondiente y resuelve los ejercicios
5. Ejecuta el archivo para comprobar tus resultados

## Requisitos

- Python 3.10 o superior
- VSCode con la extensión de Python (recomendado)
- Jupyter Notebook o la extensión Jupyter en VSCode (para los notebooks)

## Orden recomendado

Sigue los archivos en orden numérico, ya que cada tema se apoya en el anterior.
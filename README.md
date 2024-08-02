# Prueba  te4msupp0rt

## Estructura del Proyecto

```
mi_proyecto/
├── notebooks/
│   └── pregunta3.ipynb   └
│   └── pregunta4.ipynb
    └── pregunta5.ipynb
├── src/
│   ├── __init__.py
│   ├── pregunta_1/
│   │   └── obtener_dominio.py
│   └── pregunta_2/
│       └── identificar_nivel_ventas.py
├── tests/
│   ├── __init__.py
│   ├── test_obtener_dominio.py
│   └── test_identificar_nivel_ventas.py
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/mn-ariel/prueba.git
cd prueba
```

### Crear un entorno virtual y activarlo

```bash
python -m venv venv
source venv/bin/activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
pip install -e .
```

## Soluciones

### Preguntas 1 y 2 estan en el directorio `src`

El script `src/pregunta_1/obtener_dominio.py` contiene la solucion la primera pregunta.

El script `src/pregunta_1/identificar_nivel_ventas.py` contiene la solucion la segunda pregunta.

### Pruebas para las preguntas 1 y 2

Para ejecutar las pruebas, utiliza `pytest`:

```bash
pytest tests/
```

### Preguntas 3, 4 y 5 estan en el directorio `notebooks`

Los notebooks se encuentran en la carpeta `notebooks/` y contienen las soluciones de las preguntas 3, 4 y 5.

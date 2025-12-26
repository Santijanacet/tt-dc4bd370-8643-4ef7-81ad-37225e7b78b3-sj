# Prueba Técnica – tt-dc4bd370-8643-4ef7-81ad-37225e7b78b3-sj

## Política sobre el uso de Inteligencia Artificial

De acuerdo con las instrucciones de la prueba, declaro de forma explícita el uso de herramientas de Inteligencia Artificial.

### ¿Se utilizó IA?
Sí.

### Modelos utilizados
- Claude (Anthropic)
- ChatGPT (OpenAI)

### Herramientas utilizadas
- Claude vía navegador web
- ChatGPT vía navegador web
- VS Code

### ¿Para qué se utilizó la IA?
- Comprender mejor los enunciados de los problemas
- Explorar enfoques algorítmicos y validar complejidad temporal
- Revisar buenas prácticas de diseño y testing con `pytest`
- Mejorar claridad en las explicaciones y documentación
- Refactorizar código para mayor legibilidad

### ¿Para qué NO se utilizó la IA?
- No se utilizó para copiar soluciones sin análisis
- No se utilizó para generar código final sin comprensión
- No se utilizó para evadir el razonamiento propio

### Prompts utilizados (resumen)
- "Explícame posibles enfoques algorítmicos para resolver este problema"
- "Ayúdame a identificar casos borde relevantes para las pruebas"
- "Revisa esta solución en Python y sugiere mejoras de legibilidad"
- "Valida la complejidad temporal y espacial de este enfoque"
- "Sugiere cómo estructurar pruebas unitarias con pytest"
- "Ayúdame a redactar una explicación técnica clara de la solución"

### Aclaración final
Todo el código fue analizado, entendido y adaptado manualmente. La IA se utilizó exclusivamente como herramienta de apoyo y validación, manteniendo la autoría y responsabilidad total de la solución.

---

## Tiempo de resolución

El tiempo total aproximado para resolver la prueba fue de **5 horas**, incluyendo:
- Análisis del problema
- Diseño de la solución
- Implementación
- Creación de tests
- Documentación

---

## Requisitos

- Python 3.10 o superior
- pip
- pytest

---

## Cómo ejecutar la solución

La solución está pensada principalmente para ser evaluada mediante tests automatizados.

No obstante, los archivos pueden ejecutarse directamente:

```bash
python src/problema_A.py
python src/problema_B.py
```

---

## Ejecución de los tests

Los tests están implementados utilizando **pytest**.

### Ejecutar todos los tests

Desde la raíz del proyecto:

```bash
python -m pytest -v
```

### Ejecutar todos los tests de un problema específico

```bash
python -m pytest tests/test_problema_A.py -v
python -m pytest tests/test_problema_B.py -v
```

### Ejecutar un solo test

```bash
python -m pytest tests/test_problema_A.py::nombre_del_test -v
```

---

## Estructura del proyecto

```
.
├── src/
│   ├── problema_A.py
│   └── problema_B.py
├── tests/
│   ├── test_problema_A.py
│   └── test_problema_B.py
├── README.md
├── SOLUTION.md
└── LICENSE
```

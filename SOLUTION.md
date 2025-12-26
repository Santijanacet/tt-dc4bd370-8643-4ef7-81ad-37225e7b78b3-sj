
# SOLUTION – Explicación Técnica

##  Enfoque general

La prueba se abordó priorizando:
- Claridad del código
- Correctitud
- Cobertura de casos borde
- Facilidad de testeo
- Cumplimiento estricto del enunciado

Cada problema fue resuelto de manera independiente y acompañado de tests unitarios.


## Problema A – Mínimo número de salas de reuniones

### Estrategia
Se utilizó un **algoritmo de barrido de eventos (sweep line)**:
- Cada reunión genera dos eventos: inicio (+1) y fin (-1)
- Los eventos se ordenan por tiempo
- Se lleva un contador de salas activas
- El valor máximo alcanzado corresponde al mínimo número de salas necesarias

Los eventos de finalización se procesan antes que los de inicio si coinciden en el mismo minuto, evitando salas innecesarias.

### Complejidad
- Tiempo: **O(n log n)**
- Espacio: **O(n)**

---

## Problema B – Caché en memoria con TTL y política LRU

### Decisiones de diseño
- Se utilizó `OrderedDict` para implementar LRU eficientemente
- Cada entrada almacena:
  - Valor
  - Momento de expiración
- El TTL se renueva al acceder a un elemento
- Los expirados se eliminan de forma perezosa al acceder o insertar

### Métricas registradas
- Llamadas totales
- Expiraciones por TTL
- Desalojos por política LRU

---

##  Estrategia de testing

Los tests cubren:
- Inserción y recuperación básica
- Actualización de claves existentes
- Eliminación
- Claves inexistentes
- Expiración por TTL
- Renovación del TTL al acceder
- Desalojo LRU por capacidad
- Obtención de claves y valores
- Verificación de estadísticas internas

Cada test valida **un único comportamiento**, facilitando el diagnóstico de fallos.


##  Uso de IA en la solución

La IA fue utilizada como **herramienta de apoyo**, no como reemplazo del razonamiento:

- Ayudó a validar enfoques algorítmicos
- Sugirió estructura inicial de tests
- Apoyó en identificar casos borde
- Mejoró la claridad de explicaciones

Todas las decisiones finales, ajustes de código y estructura del proyecto fueron realizadas manualmente.

---

## Posibles mejoras

- Manejo de TTL por clave configurable
- Persistencia opcional del caché
- Uso de monotonic clock para mayor precisión temporal
- Cobertura de tests con mocks de tiempo para evitar `sleep`


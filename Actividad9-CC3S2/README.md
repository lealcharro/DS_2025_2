# Actividad 9

## Ejecución

### Requisitos previos

- **Versión de Python**: Python 3.12.3

### Pasos para ejecutar las pruebas

1. **Crear entorno virtual**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   make deps
   ```

<img width="1359" height="728" alt="image" src="https://github.com/user-attachments/assets/7fc9fd72-c54b-43c7-8aaa-95d6b9aa789a" />

3. **Ejecutar todas las pruebas**:
   ```bash
   make test_all
   ```

<img width="1401" height="590" alt="image" src="https://github.com/user-attachments/assets/ea3d9380-aab8-4d29-af68-237b95a1a4ec" />

4. **Ejecutar pruebas con cobertura**:
   ```bash
   make cov
   ```

<img width="1107" height="246" alt="image" src="https://github.com/user-attachments/assets/18a22904-fb62-4ee9-a172-f92b01e0c1e6" />

---

## Descripción del uso de las herramientas


**aserciones_pruebas/** - Se trabajó con pruebas básicas de una clase Stack usando assertEqual, assertTrue y assertFalse. Las pruebas verifican operaciones como push, pop, peek y si está vacía. Se agregó mensajes descriptivos a cada aserción para que cuando algo falle sea más fácil saber qué pasó.

**pruebas_fixtures/** - Esta parte fue interesante porque se usaron fixtures para preparar el ambiente antes de cada test. setup_class carga los datos desde account_data.json una sola vez, y setup_method limpia la base de datos antes de cada prueba individual. teardown_method elimino la sesión después. Esto permite tener cada test completamente aislado del anterior.

**coverage_pruebas/** - Acá se midió qué tan bien están cubiertas las pruebas. Se configura pytest-cov para que mida cobertura de sentencias, ramas, funciones y condiciones. Los reportes HTML ayudan bastante para ver exactamente qué líneas faltan.

**factories_fakes/** - Se usó FactoryBoy para generar datos de prueba en vez de hardcodear. Con Faker se generan nombres, emails y teléfonos realistas, y con FuzzyChoice y FuzzyDate se crean datos aleatorios para fechas y booleanos. Esto hizo que las pruebas sean más robustas porque ahora se puede generar cientos de casos de prueba sin escribir cada uno manualmente.

**mocking_objetos/** - Se simuló llamadas a la API de IMDb porque es más práctico que hacer requests reales en cada test. Se usa @patch para interceptar las llamadas y Mock para simular respuestas. Se guardaron algunas respuestas reales de la API en imdb_responses.json y se usaron como fixtures. Se probó casos como búsqueda exitosa, búsqueda sin resultados (404), y errores de API.

**practica_tdd/** - Se implementa una API REST de contadores siguiendo TDD. Primero se escribe test (que fallaba al inicio porque falta la implemetación), luego lo mínimo para que pase, y después refactorizar. Al final se agregó un decorador @require_counter para no repetir la validación en cada endpoint. Se agregan rutas para crear, obtener, actualizar, eliminar, incrementar, setear valor específico, listar todos y resetear contadores.

## Resultados

- En total hay 46 tests repartidos 7 módulos de prueba en las carpetas. 

- El coverage llegó a 100% en models/__init__.py y models/account.py con cobertura de ramas activada.
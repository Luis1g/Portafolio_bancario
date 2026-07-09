#  Terminal de Análisis de Riesgo Financiero

Un microservicio full-stack diseñado para la consulta de activos financieros, procesamiento de series de tiempo y cálculo de métricas de riesgo institucional. 

Este proyecto demuestra la implementación de una arquitectura limpia separando el motor de cálculo (Backend) de la visualización interactiva (Frontend).

##  Características Principales

* **Cálculo de Riesgo Institucional:** Procesa datos históricos (252 días bursátiles) para calcular la Volatilidad Anualizada y el Máximo Drawdown (Max Drawdown) de cualquier activo.
* **Series de Tiempo en Tiempo Real:** Consumo de datos de mercado automatizado mediante `yfinance` y procesamiento matricial con `pandas` y `numpy`.
* **Gráficos de Alto Rendimiento:** Integración de `Lightweight Charts` (TradingView) para renderizar gráficas interactivas en Canvas de forma fluida.
* **Manejo Estricto de Errores:** Validación de inputs y manejo de excepciones HTTP (400, 404, 500) para asegurar que la terminal nunca colapse ante datos inválidos.
* **Cobertura de Pruebas:** Pruebas unitarias implementadas para garantizar la exactitud matemática de las respuestas de la API.

##  Stack Tecnológico

**Backend (Motor de Datos):**
* **Python 3.x**
* **FastAPI:** Framework moderno y asíncrono para la construcción de la API REST.
* **Pandas & NumPy:** Limpieza de datos y cálculos matemáticos vectorizados.
* **Pytest:** Framework para pruebas unitarias.
* **Uvicorn:** Servidor ASGI para ejecución en desarrollo y producción.

**Frontend (Interfaz de Usuario):**
* **HTML5 & CSS3:** Diseño responsivo "Dark Mode" inspirado en terminales profesionales de trading (ej. Bloomberg).
* **Vanilla JavaScript:** Consumo de API mediante promesas (`async/await`) y la API `fetch`.
* **Lightweight Charts:** Librería gráfica optimizada para series de tiempo financieras.

##  Instalación y Ejecución Local

Sigue estos pasos para replicar el entorno en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
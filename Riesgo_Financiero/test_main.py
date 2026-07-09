from fastapi.testclient import TestClient
from main import app

# Inicializamos el cliente de pruebas de FastAPI
# Esto simula peticiones HTTP sin necesidad de levantar el servidor real
client = TestClient(app)

def test_analizar_riesgo_ticker_valido():
    """
    Escenario de Éxito (Camino Feliz): 
    Se envía un ticker válido y se espera un código HTTP 200 con la estructura JSON correcta.
    """
    respuesta = client.get("/api/analisis/AAPL")
    
    # 1. Validamos que el servidor responda correctamente
    assert respuesta.status_code == 200
    
    # 2. Convertimos la respuesta a un diccionario de Python
    datos = respuesta.json()
    
    # 3. Validamos que la estructura de datos sea exactamente la que el frontend espera
    assert datos["ticker"] == "AAPL"
    assert "nombre_empresa" in datos
    assert "precio_actual" in datos
    
    # 4. Validamos que las métricas de riesgo existan y sean números (float)
    assert "metricas_riesgo" in datos
    assert isinstance(datos["metricas_riesgo"]["volatilidad_anualizada_porcentaje"], float)
    assert isinstance(datos["metricas_riesgo"]["max_drawdown_porcentaje"], float)
    
    # 5. Validamos que el histórico para la gráfica sea una lista
    assert "historico" in datos
    assert isinstance(datos["historico"], list)

def test_analizar_riesgo_ticker_invalido():
    """
    Escenario de Error (Camino Triste): 
    Se envía un ticker que no existe y se espera un código HTTP 404 manejado limpiamente.
    """
    # Usamos un ticker que sabemos que no existe
    respuesta = client.get("/api/analisis/FALSO12345")
    
    # 1. Validamos que nuestro manejo de errores (HTTPException) esté funcionando
    assert respuesta.status_code == 404
    
    # 2. Validamos que el mensaje de error sea descriptivo
    datos = respuesta.json()
    assert "detail" in datos
    assert "Ticker inválido o sin datos" in datos["detail"]
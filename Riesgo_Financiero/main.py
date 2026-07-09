from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import numpy as np

app = FastAPI(title="API de Análisis Financiero Pro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/analisis/{ticker}")
def analizar_riesgo_accion(ticker: str):
    try:
        # 1. Traemos el histórico de 1 año
        accion = yf.Ticker(ticker)
        df = accion.history(period="1y")
        
        if df.empty:
            raise HTTPException(status_code=404, detail=f"Ticker inválido o sin datos: {ticker}")
            
        # 2. Precio de cierre más reciente
        precio_actual = round(df['Close'].iloc[-1], 2)
        
        # 3. y 4. Cálculos de Riesgo
        df['Rendimientos'] = df['Close'].pct_change()
        volatilidad_anualizada = df['Rendimientos'].std() * np.sqrt(252)
        
        # 5. Máximo Drawdown
        picos_historicos = df['Close'].cummax()
        caidas = (df['Close'] - picos_historicos) / picos_historicos
        max_drawdown = caidas.min()

        # 6. PREPARACIÓN DE DATOS PARA LA GRÁFICA (NUEVO)
        # Lightweight Charts requiere un formato exacto: [{"time": "YYYY-MM-DD", "value": 150.5}, ...]
        df_historico = df.reset_index() # Sacamos la fecha del índice para poder usarla
        datos_grafica = []
        
        for index, row in df_historico.iterrows():
            # Convertimos la fecha (Datetime) a texto en formato YYYY-MM-DD
            fecha_str = row['Date'].strftime('%Y-%m-%d')
            precio = round(row['Close'], 2)
            datos_grafica.append({"time": fecha_str, "value": precio})

        # 7. Formateamos la respuesta final, ahora incluyendo 'historico'
        return {
            "ticker": ticker.upper(),
            "nombre_empresa": accion.info.get("longName", "Desconocido"),
            "moneda": accion.info.get("currency", "USD"),
            "precio_actual": precio_actual,
            "metricas_riesgo": {
                "volatilidad_anualizada_porcentaje": round(volatilidad_anualizada * 100, 2),
                "max_drawdown_porcentaje": round(max_drawdown * 100, 2)
            },
            "historico": datos_grafica # Mandamos el arreglo de puntos al frontend
        }
        
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
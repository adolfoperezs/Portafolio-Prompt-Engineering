#!/usr/bin/env python3
"""
Funciones para obtener datos de inflación del IPC de Chile desde Mindicador.cl
"""

import requests
from datetime import datetime

API_URL = "https://mindicador.cl/api/ipc"
MIN_YEAR = 1980

def fetch_ipc_series() -> list:
    """
    Descarga la serie completa de datos del IPC desde la API.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lanza un error para códigos 4xx/5xx
        data = response.json()
        return data.get('serie', [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con la API: {e}")
        return []

def find_index_for_year(ipc_series: list, year: int) -> float | None:
    """
    Encuentra el primer índice de IPC disponible para un año específico.
    Busca el valor de Enero, si no, el primer mes que encuentre.
    """
    for record in reversed(ipc_series): # Revertido para buscar del más antiguo al más nuevo
        # Se reemplaza la 'Z' para compatibilidad con versiones de Python < 3.11
        date_str = record['fecha'].replace('Z', '+00:00')
        record_date = datetime.fromisoformat(date_str)
        if record_date.year == year:
            return record['valor']
    return None

def get_latest_index(ipc_series: list) -> float | None:
    """
    Obtiene el índice de IPC más reciente de la serie.
    """
    if ipc_series:
        return ipc_series[0]['valor']
    return None

def get_inflation_factor(year: int) -> float | None:
    """
    Calcula el factor de inflación entre un año base y el presente.
    Factor = Indice_Reciente / Indice_Año_Base
    """
    current_year = datetime.now().year
    if not (MIN_YEAR <= year < current_year):
        print(f"❌ Error: El año debe estar entre {MIN_YEAR} y {current_year - 1}.")
        return None

    print("🔄 Obteniendo datos de inflación...")
    ipc_series = fetch_ipc_series()

    if not ipc_series:
        return None

    latest_ipc = get_latest_index(ipc_series)
    base_ipc = find_index_for_year(ipc_series, year)

    if latest_ipc is None or base_ipc is None:
        print(f"❌ No se encontraron datos suficientes para el año {year}.")
        return None
    
    if base_ipc == 0:
        print("❌ Error: El índice base es cero, no se puede dividir.")
        return None

    factor = latest_ipc / base_ipc
    print("✅ Factor de inflación calculado con éxito.")
    return factor 
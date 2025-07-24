#!/usr/bin/env python3
"""
Funciones para obtener datos de inflación del IPC de Chile desde Mindicador.cl
"""

import requests
from datetime import datetime

API_BASE_URL = "https://mindicador.cl/api/uf" # Cambiado de IPC a UF
MIN_YEAR = 1977 # La UF existe desde 1977

def fetch_series(year: int) -> list:
    """
    Descarga la serie de datos de la UF para un año específico.
    """
    try:
        url = f"{API_BASE_URL}/{year}"
        print(f"🔄 Obteniendo datos desde la URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('serie', [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con la API: {e}")
        return []

def find_first_value_for_year(series: list, year: int) -> float | None:
    """
    Encuentra el primer valor de la UF disponible para un año específico.
    """
    for record in reversed(series):
        try:
            date_only_str = record['fecha'][:10]
            record_date = datetime.strptime(date_only_str, '%Y-%m-%d')
            if record_date.year == year:
                return record['valor']
        except (ValueError, KeyError, IndexError):
            continue
    return None

def get_latest_value(series: list) -> float | None:
    """
    Obtiene el valor más reciente de la UF de la serie.
    """
    if series:
        return series[0]['valor']
    return None

def get_inflation_factor(year: int) -> float | None:
    """
    Calcula el factor de ajuste basado en el valor de la UF.
    """
    current_year = datetime.now().year
    if not (MIN_YEAR <= year <= current_year):
        print(f"❌ Error: El año debe estar entre {MIN_YEAR} y {current_year}.")
        return None

    # --- Búsqueda del valor más reciente ---
    latest_value = None
    for year_to_try in range(current_year, MIN_YEAR - 1, -1):
        # print(f"Buscando el valor más reciente en el año {year_to_try}...")
        latest_series = fetch_series(year_to_try)
        if latest_series:
            latest_value_candidate = get_latest_value(latest_series)
            if latest_value_candidate is not None and latest_value_candidate > 0:
                latest_value = latest_value_candidate
                print(f"✅ Valor más reciente encontrado para {year_to_try}: ${latest_value:,.2f}")
                break

    if latest_value is None:
        print("❌ No se pudo encontrar un valor de UF reciente.")
        return None

    # --- Obtención del valor base ---
    base_series = fetch_series(year)
    if not base_series:
        print(f"❌ No se encontraron datos para el año base {year}.")
        return None
    base_value = find_first_value_for_year(base_series, year)
    
    if base_value is None:
        print(f"❌ No se encontraron datos suficientes para el año {year}.")
        return None
    
    if base_value == 0:
        print("❌ Error: El valor base es cero, no se puede dividir.")
        return None

    factor = latest_value / base_value
    print("✅ Factor de ajuste calculado con éxito.")
    return factor 
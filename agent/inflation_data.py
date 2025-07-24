#!/usr/bin/env python3
"""
Funciones para obtener datos de inflación.
"""

import requests

def get_inflation_data(country: str, year: int) -> float:
    """
    Obtiene el dato de inflación para un país y año específicos.
    NOTA: Esta es una función de ejemplo y necesita una API real.
    """
    print(f"Buscando datos de inflación para {country} en {year}...")
    # Lógica para conectar a una API de datos de inflación (ej. Banco Mundial)
    # Por ahora, devolvemos un valor fijo para el ejemplo.
    return 5.0 
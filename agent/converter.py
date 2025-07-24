#!/usr/bin/env python3
"""
Lógica para los cálculos de conversión de moneda ajustada por inflación.
"""

def adjust_for_inflation(amount: float, inflation_rate: float, years: int) -> float:
    """
    Ajusta una cantidad de dinero por la tasa de inflación a lo largo de los años.
    """
    adjusted_amount = amount * ((1 + inflation_rate / 100) ** years)
    return adjusted_amount 
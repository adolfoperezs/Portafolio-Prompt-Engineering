#!/usr/bin/env python3
"""
Herramienta de LangChain para el cálculo de inflación.
"""
import re
from langchain.agents import Tool # Correcto para versiones más nuevas
from agent.inflation_data import get_inflation_factor

def inflation_calculator_func(input_str: str) -> str:
    """
    Parsea el input del usuario para extraer el monto y el año,
    y devuelve el cálculo de inflación.
    """
    # Limpiar el input de comas para facilitar la extracción de números
    cleaned_input = input_str.replace(",", "").replace("$", "")
    
    # Usamos regex para encontrar números en el input limpio
    numbers = re.findall(r'\d+', cleaned_input)
    
    if len(numbers) < 2:
        return "Error: No se encontró un monto y un año. Se necesitan ambos."
        
    try:
        # Tomamos los dos primeros números encontrados
        amount = float(numbers[0])
        year = int(numbers[1])
    except ValueError:
        return "Error: No se pudieron interpretar los números como monto y año."

    factor = get_inflation_factor(year)
    
    if factor is None:
        return f"Error: No se pudo calcular la inflación para el año {year}. Verifica que el año sea válido."
        
    converted_amount = amount * factor
    
    # Devolver un string simple y fáctico, no una frase para el usuario final.
    # El agente usará esto para construir la respuesta final.
    return f"El monto original de {amount} del año {year} equivale a {converted_amount:.2f} hoy (Factor: {factor:.4f})."


inflation_tool = Tool(
    name="InflationCalculator",
    func=inflation_calculator_func,
    description=(
        "Útil para calcular el valor ajustado por inflación de una cantidad de dinero (pesos chilenos) "
        "de un año específico al valor actual. La entrada debe ser una frase que contenga un monto y un año. "
        "Devuelve una frase con el resultado del cálculo."
    )
) 
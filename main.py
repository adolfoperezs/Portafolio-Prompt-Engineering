#!/usr/bin/env python3
"""
Calculadora de Inflación con Agente de IA
Punto de entrada principal del proyecto
"""

import os
from dotenv import load_dotenv
from agent.inflation_data import get_inflation_factor

# Cargar variables de entorno
load_dotenv()

def main():
    """Función principal para la calculadora de inflación"""
    print("💰 Calculadora de Inflación para Chile (CLP)")
    print("=" * 50)
    print("Esta herramienta convierte un monto en pesos chilenos de un año pasado a su valor equivalente hoy, usando datos del IPC.")
    print("-" * 50)

    try:
        amount_str = input("➡️  Ingresa el monto original (ej: 10000): ")
        amount = float(amount_str)

        year_str = input("➡️  Ingresa el año base (ej: 1990): ")
        year = int(year_str)

        factor = get_inflation_factor(year)

        if factor is not None:
            converted_amount = amount * factor
            print("\n" + "="*50)
            print(f"📈 Resultado:")
            print(f"Un monto de ${amount:,.0f} en el año {year} equivale a")
            print(f"aproximadamente ${converted_amount:,.0f} pesos de hoy.")
            print("="*50)

    except ValueError:
        print("❌ Error: Por favor, ingresa un número válido para el monto y el año.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main() 
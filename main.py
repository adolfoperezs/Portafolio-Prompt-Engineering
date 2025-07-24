#!/usr/bin/env python3
"""
Calculadora de Inflación con Agente de IA
Punto de entrada principal del proyecto
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def main():
    """Función principal del agente de IA"""
    print("🤖 Agente de IA - Calculadora de Inflación")
    print("=" * 50)
    print("Proyecto inicializado correctamente")
    print("Estructura básica creada")
    
    # Verificar que las API keys estén configuradas
    openai_key = os.getenv('OPENAI_API_KEY')
    if not openai_key:
        print("⚠️  Recordatorio: Configura tu OPENAI_API_KEY en el archivo .env")
    else:
        print("✅ API Key de OpenAI configurada")

if __name__ == "__main__":
    main() 
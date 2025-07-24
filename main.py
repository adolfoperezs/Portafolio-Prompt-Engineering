#!/usr/bin/env python3
"""
Agente Conversacional para Calcular Inflación con LangChain
"""
import os
from dotenv import load_dotenv, find_dotenv

# Cargar las variables de entorno
load_dotenv(find_dotenv(usecwd=True))
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("🛑 ERROR: La variable de entorno OPENAI_API_KEY no está configurada o no se pudo leer.")
    exit()

from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from agent.tool import inflation_tool

def main():
    """Punto de entrada principal del agente conversacional."""
    print("🤖 ¡Hola! Soy el Agente de Inflación.")
    print("Puedo ayudarte a calcular el valor del dinero en el tiempo.")
    print("="*50)

    # 1. Configuración del LLM
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    # 2. Definir herramientas
    tools = [inflation_tool]

    # 3. Cargar el prompt del sistema desde LangChain Hub
    prompt = hub.pull("hwchase17/react")

    # 4. Crear el agente
    agent = create_react_agent(llm, tools, prompt)

    # 5. Crear el Ejecutor del Agente
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        handle_parsing_errors=True # Maneja errores de parseo de forma robusta
    )

    # Bucle interactivo
    while True:
        try:
            user_input = input("➡️  ¿Qué te gustaría calcular? (o escribe 'salir'): ")
            if user_input.lower() in ("salir", "exit", "quit"):
                print("👋 ¡Hasta luego!")
                break
            
            if user_input.strip():
                response = agent_executor.invoke({"input": user_input})
                print("\n✅ Respuesta del Agente:")
                print(response['output'])
                print("-" * 50)

        except Exception as e:
            print(f"💥 Ha ocurrido un error: {e}")
            print("Vamos a intentarlo de nuevo.")

if __name__ == "__main__":
    main() 
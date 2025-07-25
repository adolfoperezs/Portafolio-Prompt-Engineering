# 🤖 Agente Calculador de Inflación con LangChain

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-brightgreen?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple?style=for-the-badge&logo=openai)

---

### **[ 🎬 Inserta aquí un GIF de demostración del agente funcionando ]**

Este proyecto es un agente conversacional de IA construido con Python y LangChain, diseñado para calcular el valor del dinero ajustado por la inflación en Chile. El agente utiliza el modelo `gpt-4o-mini` de OpenAI para entender las preguntas de los usuarios en lenguaje natural y una herramienta personalizada que se conecta a una API pública para obtener datos financieros en tiempo real.

Este repositorio no solo muestra el resultado final, sino también el **proceso de desarrollo iterativo**, incluyendo la depuración de dependencias, la refactorización de código y la resolución de problemas lógicos del agente, reflejando un ciclo de vida de desarrollo de software realista.

## 🚀 Características Principales

*   **Interfaz Conversacional:** Permite a los usuarios realizar consultas de forma natural, como *"¿cuánto serían 10.000 pesos de 1995 hoy?"*.
*   **Uso de Herramientas (Tools) de LangChain:** El agente está equipado con una herramienta (`Tool`) que encapsula la lógica para buscar datos y realizar cálculos matemáticos.
*   **Integración de API Externa:** Se conecta a la API pública de [Mindicador.cl](https://mindicador.cl/api-banco-central) para obtener el valor histórico de la Unidad de Fomento (UF), usada como índice de inflación.
*   **Modelo de Lenguaje Avanzado:** Utiliza `gpt-4o-mini` para el razonamiento, la toma de decisiones (qué herramienta usar) y la generación de respuestas finales para el usuario.
*   **Manejo Robusto de Errores:** El agente y las herramientas están diseñados para gestionar entradas incorrectas, años fuera de rango y posibles fallos de la API.

## 🛠️ Stack Tecnológico

*   **Lenguaje:** Python
*   **Framework de Agente IA:** LangChain
*   **Modelo de Lenguaje (LLM):** OpenAI - `gpt-4o-mini`
*   **Fuente de Datos:** API REST de [Mindicador.cl](https://mindicador.cl/api-banco-central)
*   **Gestión de Dependencias:** Pip y Entorno Virtual (`venv`)

## ⚙️ Instalación y Uso

Para ejecutar este agente en tu máquina local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/adolfoperezs/Agente-calculador-inflacion.git
    cd Agente-calculador-inflacion
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Crearemos el archivo `requirements.txt` en el siguiente paso)*

4.  **Configura tu clave de API:**
    *   Crea un archivo llamado `.env` en la raíz del proyecto.
    *   Añade tu clave de API de OpenAI al archivo de esta forma:
        ```env
        OPENAI_API_KEY="tu_clave_secreta_aqui"
        ```

5.  **Ejecuta el agente:**
    ```bash
    python main.py
    ```
    ¡Ahora puedes empezar a chatear con el agente!

## 💡 Proceso y Aprendizajes

El desarrollo de este agente fue un ejercicio práctico en la resolución de problemas del mundo real:
*   **Conflicto de Dependencias:** Se encontró y resolvió un complejo problema de incompatibilidad entre las versiones de `langchain`, `pydantic` y `langsmith`, lo que requirió una reconstrucción completa del entorno virtual con versiones fijas.
*   **Elección de la Fuente de Datos:** Inicialmente se usó la API de IPC, pero las pruebas revelaron que devolvía datos de variación en lugar de un índice absoluto. Se investigó y se pivotó hacia la API de la UF, que resultó ser una fuente de datos mucho más fiable para el cálculo.
*   **Diseño de Herramientas (Tools):** Se aprendió que las herramientas de LangChain deben devolver datos "crudos" y fácticos, dejando la tarea de "comunicación" y formateo de la respuesta final al agente LLM para evitar bucles.

---

Creado por Adolfo Pérez. 
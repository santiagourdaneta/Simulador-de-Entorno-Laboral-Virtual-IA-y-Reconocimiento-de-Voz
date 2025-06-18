
Simulador interactivo de tareas laborales con IA para feedback y entrada de voz. Ideal para practicar habilidades profesionales en un entorno virtual.

# Simulador de Entorno Laboral Virtual 🚀

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-lightgrey.svg)](https://pypi.org/project/SpeechRecognition/)
[![Pydub](https://img.shields.io/badge/Pydub-orange.svg)](https://pypi.org/project/pydub/)

## Descripción del Proyecto

El **Simulador de Entorno Laboral Virtual** es una innovadora plataforma interactiva diseñada para ayudar a usuarios a **practicar y mejorar sus habilidades profesionales** en un contexto simulado. Utilizando **inteligencia artificial (IA)** para proporcionar **feedback instantáneo** y **reconocimiento de voz** para la interacción, este simulador permite a los usuarios enfrentarse a diversas **tareas laborales** y recibir una evaluación sobre la calidad de sus respuestas.

Es una herramienta ideal para estudiantes, recién graduados o profesionales que buscan **desarrollar competencias clave** como la comunicación efectiva, la resolución de problemas y la toma de decisiones en un **ambiente de aprendizaje sin riesgos**.

## Características Principales ✨

* **Simulación de Tareas Reales:** Enfréntate a una variedad de escenarios y desafíos comunes en el ámbito laboral (redacción de correos, organización de agendas, respuesta a clientes, análisis de datos, etc.).
* **Entrada de Voz y Texto:** Responde a las tareas dictando tu respuesta por voz (gracias a la integración con Google Speech-to-Text) o escribiéndola directamente.
* **Feedback Inteligente con IA:** Recibe una evaluación automatizada sobre la similitud de tu respuesta con la solución esperada, con un porcentaje de coincidencia y consejos útiles.
* **Sistema de Reconocimiento de Voz:** Transcripción de audio a texto robusta para una interacción natural.
* **Basado en Django:** Un framework web robusto y seguro para el backend.

## ¿Cómo Empezar? (Guía Rápida) 🚀

Para poner en marcha el simulador en tu máquina local, sigue estos pasos:

### 1. Requisitos Previos

Asegúrate de tener instalado:

* **Python 3.8+**
* **pip** (gestor de paquetes de Python)
* **FFmpeg:** Necesario para el procesamiento de audio. Descárgalo desde [ffmpeg.org](https://ffmpeg.org/download.html) (para Windows, se recomienda una build como las de [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)). Asegúrate de que `ffmpeg.exe` y `ffprobe.exe` estén accesibles en tu `PATH` o especifica su ruta en `views.py`.

### 2. Clonar el Repositorio

```bash
git clone https://github.com/santiagourdaneta/Simulador-de-Entorno-Laboral-Virtual-IA-y-Reconocimiento-de-Voz/
cd Simulador-de-Entorno-Laboral-Virtual-IA-y-Reconocimiento-de-Voz

3. Crear y Activar un Entorno Virtual (Recomendado)
Bash

python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

4. Instalar Dependencias
Bash

pip install -r requirements.txt

5. Configuración de FFmpeg en views.py (Si no está en PATH)
Si FFmpeg no está en tu PATH de sistema, abre tareas_simulacion/views.py y descomenta/ajusta las siguientes líneas al inicio del archivo con la ruta correcta a tus ejecutables ffmpeg.exe y ffprobe.exe (usando barras /):

# from pydub import AudioSegment
# AudioSegment.ffmpeg = "C:/ruta/a/tu/ffmpeg-build/bin/ffmpeg.exe"
# AudioSegment.ffprobe = "C:/ruta/a/tu/ffmpeg-build/bin/ffprobe.exe"
(Si lo tienes en el PATH, asegúrate de que estas líneas estén comentadas #)

6. Aplicar Migraciones
Bash

python manage.py makemigrations tareas_simulacion
python manage.py migrate

7. Crear Superusuario (Opcional, para acceder al Admin)
Bash

python manage.py createsuperuser

8. Cargar Tareas de Demostración (Opcional, pero recomendado)
Para poblar tu base de datos con tareas de ejemplo:

Bash

python manage.py crear_tareas_demo
9. Ejecutar el Servidor
Bash

python manage.py runserver
Una vez que el servidor esté corriendo, abre tu navegador y visita http://127.0.0.1:8000/

Estructura del Proyecto 📂
simulador/
├── tareas_simulacion/        # Aplicación principal del simulador
│   ├── migrations/
│   ├── management/           # Comandos personalizados de Django (ej. crear_tareas_demo)
│   │   └── commands/
│   │       └── crear_tareas_demo.py
│   ├── templates/
│   │   └── tareas_simulacion/
│   │       └── tarea.html    # Frontend con HTML, CSS, JS para interacción
│   ├── __init__.py
│   ├── admin.py              # Configuración para el panel de administración
│   ├── models.py             # Definición de la TareaSimulacion
│   ├── views.py              # Lógica del backend, procesamiento de audio y feedback
│   └── urls.py               # Rutas de la aplicación
├── simulador/                # Configuración global del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py                 # Utilidad de línea de comandos de Django
└── README.md                 # Este archivo

Contribuciones 🤝
¡Las contribuciones son bienvenidas! Si tienes ideas para nuevas características, mejoras o corrección de errores, no dudes en abrir un issue o enviar un pull request.

Palabras clave: "interactivo", "tareas laborales", "IA", "feedback", "entrada de voz", "practicar habilidades profesionales", "entorno virtual", "Simulador", "Entorno Laboral", "Virtual", "IA", "Reconocimiento de Voz".


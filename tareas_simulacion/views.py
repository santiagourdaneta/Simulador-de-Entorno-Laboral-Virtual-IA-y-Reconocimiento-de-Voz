import random # Añade esta línea al inicio
from django.shortcuts import render
from .models import TareaSimulacion
import difflib
import speech_recognition as sr
import os
from pydub import AudioSegment # Importamos pydub para la conversión de audio

# Opcional: Si pydub no encuentra FFmpeg automáticamente, descomenta la línea de abajo
# y pon la ruta correcta a tu ejecutable ffmpeg.exe
#AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
#AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe" # También podrías necesitar ffprobe

def mostrar_tarea(request):
    tarea = None
    feedback_ia = None
    respuesta_transcrita = "" # Almacena el texto si se usó la voz
    mensaje_error_audio = None # Para mostrar errores específicos del procesamiento de audio

    try:
        # Obtiene todas las tareas disponibles
        todas_las_tareas = TareaSimulacion.objects.all()
        if todas_las_tareas.exists():
            # Selecciona una tarea aleatoria de la lista
            tarea = random.choice(list(todas_las_tareas))
        else:
            pass # No hay tareas, 'tarea' se queda como None
    except TareaSimulacion.DoesNotExist:
        pass # Esto ya no debería ocurrir con .exists() y random.choice

    # Verificamos si la solicitud es de tipo POST. Esto significa que el usuario
    # ha enviado el formulario (ya sea escribiendo texto o dictando voz).
    if request.method == 'POST':
        if tarea: # Solo procesamos si hay una tarea válida para trabajar
            respuesta_usuario_para_ia = "" # Variable para la respuesta que la IA analizará

            # --- Lógica para Procesar la Respuesta Dictada por Voz ---
            # Si el navegador envió un archivo de audio (indicando que se usó la función de voz)
            if 'audio_respuesta' in request.FILES:
                audio_file = request.FILES['audio_respuesta'] # Obtenemos el archivo de audio

                # Rutas temporales para guardar el audio recibido y la versión convertida a WAV
                temp_webm_path = "temp_audio_from_browser.webm"
                temp_wav_path = "temp_audio_converted.wav"

                try:
                    # 1. Guardar el archivo WebM recibido del navegador en disco.
                    # Esto es necesario porque SpeechRecognition y pydub trabajan mejor con rutas de archivo.
                    with open(temp_webm_path, "wb") as destination:
                        for chunk in audio_file.chunks():
                            destination.write(chunk)

                    # 2. Usar pydub para convertir el archivo WebM a WAV.
                    # SpeechRecognition y PyAudio prefieren el formato WAV.
                    audio = AudioSegment.from_file(temp_webm_path, format="webm")
                    audio.export(temp_wav_path, format="wav")

                    # 3. Utilizar SpeechRecognition para transcribir el archivo WAV.
                    r = sr.Recognizer() # Creamos una instancia del reconocedor de voz
                    with sr.AudioFile(temp_wav_path) as source:
                        audio_data = r.record(source) # Leemos el audio del archivo WAV
                        # Realizamos la transcripción usando el servicio de Google Web Speech API.
                        # 'es-ES' es para español de España, puedes cambiar a 'es-MX' para México, etc.
                        respuesta_transcrita = r.recognize_google(audio_data, language='es-ES')
                        
                except sr.UnknownValueError:
                    # Este error ocurre si el servicio de reconocimiento de voz no pudo entender el audio.
                    mensaje_error_audio = "Lo siento, no pude entender bien el audio. ¿Podrías hablar más claro o escribir tu respuesta?"
                except sr.RequestError as e:
                    # Este error ocurre si hay un problema de conexión con el servicio de Google.
                    mensaje_error_audio = f"Hubo un error con el servicio de Google Speech: {e}. Asegúrate de tener conexión a internet."
                except Exception as e:
                    # Esto es un "parche" para capturar cualquier otro error inesperado,
                    # como problemas con FFmpeg o pydub.
                    mensaje_error_audio = f"Ocurrió un error inesperado al procesar el audio (conversión o lectura): {e}. Asegúrate que FFmpeg esté bien instalado y en tu PATH."
                    print(f"DEBUG: Error detallado en el backend: {e}") # Imprimirá en tu CMD para depuración
                finally:
                    # Es crucial limpiar los archivos temporales después de usarlos.
                    if os.path.exists(temp_webm_path):
                        os.remove(temp_webm_path)
                    if os.path.exists(temp_wav_path):
                        os.remove(temp_wav_path)

                # Si la transcripción fue exitosa (no hubo errores graves), usamos ese texto.
                respuesta_usuario_para_ia = respuesta_transcrita

            # --- Lógica para Procesar la Respuesta Escrita (si no se usó la voz o hubo error en ella) ---
            # Si no se recibió un archivo de audio, o si la transcripción de voz falló,
            # intentamos obtener la respuesta del campo de texto normal.
            if not respuesta_usuario_para_ia:
                respuesta_usuario_para_ia = request.POST.get('respuesta_usuario', '').strip()
                # Si hubo un error de audio pero el usuario no escribió nada,
                # nos aseguramos de que no se procese un texto vacío.
                if mensaje_error_audio and not respuesta_usuario_para_ia:
                    respuesta_usuario_para_ia = ""

            # --- Generación del Feedback de la IA (simulada) ---
            # Solo generamos feedback si hay una respuesta válida (escrita o transcrita) y una tarea.
            if respuesta_usuario_para_ia:
                respuesta_esperada = tarea.respuesta_esperada.strip()

                # Preparamos los textos para la comparación: todo a minúsculas y normalizando espacios.
                texto_usuario_limpio = ' '.join(respuesta_usuario_para_ia.lower().split())
                texto_esperado_limpio = ' '.join(respuesta_esperada.lower().split())

                # Usamos difflib.SequenceMatcher para calcular la similitud.
                matcher = difflib.SequenceMatcher(None, texto_usuario_limpio, texto_esperado_limpio)
                similitud = matcher.ratio() * 100 # Convertimos a porcentaje

                # Generamos un mensaje de feedback basado en el porcentaje de similitud.
                if similitud > 80:
                    feedback_ia = f"¡Excelente! Tu respuesta es muy completa y se parece mucho a lo esperado ({similitud:.0f}% de similitud). ¡Gran trabajo!"
                elif similitud > 50:
                    feedback_ia = f"¡Buen intento! Tu respuesta tiene puntos clave, pero podrías mejorarla. Revisa la respuesta esperada para ver qué detalles faltaron. ({similitud:.0f}% de similitud)."
                else:
                    feedback_ia = f"Hmm, tu respuesta es un poco diferente a lo que se esperaba. Te sugiero revisar la 'Respuesta Esperada' para entender mejor el enfoque. ({similitud:.0f}% de similitud)."
            else:
                # Si el usuario no proporcionó ninguna respuesta válida (ni texto ni audio exitoso).
                # Usamos el mensaje de error de audio si existe, o un mensaje genérico.
                feedback_ia = mensaje_error_audio or "Por favor, ingresa tu respuesta ya sea escribiendo o dictando por voz."

    # --- Envío de Datos a la Plantilla (SIEMPRE se ejecuta al final de la función) ---
    # Preparamos el 'contexto' (un diccionario con datos) que Django enviará a la plantilla HTML.
    context = {
        'tarea': tarea, # La tarea actual a mostrar
        'feedback_ia': feedback_ia, # El feedback generado por la IA
        'respuesta_transcrita': respuesta_transcrita, # La respuesta del usuario si fue dictada por voz
        'mensaje_error_audio': mensaje_error_audio, # Cualquier error específico del audio
    }
    # La función 'render' toma la solicitud, la ruta a la plantilla HTML, y el contexto,
    # y devuelve una respuesta HTTP que el navegador puede mostrar.
    return render(request, 'tareas_simulacion/tarea.html', context)
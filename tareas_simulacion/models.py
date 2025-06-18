from django.db import models

# Este es nuestro plano para cada tarea en el simulador
class TareaSimulacion(models.Model):
    nombre = models.CharField(max_length=200) # El nombre de la tarea (ej: "Responder email")
    descripcion = models.TextField() # Lo que se tiene que hacer en la tarea
    respuesta_esperada = models.TextField() # Lo que consideramos una buena respuesta
    dificultad = models.CharField(max_length=50) # Nivel de dificultad (ej: "Facil", "Medio")

    # Esto es para que cuando veamos la tarea, nos muestre su nombre
    def __str__(self):
        return self.nombre
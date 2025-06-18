from django.urls import path
from . import views # Importamos las "vistas" que acabamos de crear

# Aquí definimos las direcciones de nuestra aplicación
urlpatterns = [
    # Cuando alguien vaya a la dirección vacía (''), llama a la función 'mostrar_tarea'
    path('', views.mostrar_tarea, name='mostrar_tarea'),
]
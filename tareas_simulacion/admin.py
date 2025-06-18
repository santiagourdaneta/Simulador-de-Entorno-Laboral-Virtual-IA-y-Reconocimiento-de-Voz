from django.contrib import admin
from .models import TareaSimulacion # Importamos nuestro modelo

# Registramos nuestro modelo para que aparezca en el administrador
admin.site.register(TareaSimulacion)

from django.core.management.base import BaseCommand
from tareas_simulacion.models import TareaSimulacion

class Command(BaseCommand):
    help = 'Crea un conjunto de tareas de simulación de ejemplo en la base de datos.'

    def handle(self, *args, **options):
        # Lista de tareas de ejemplo que queremos añadir
        # Puedes modificar, añadir o quitar tareas de esta lista
        tareas_a_crear = [
            {
                'nombre': 'Redactar un correo de seguimiento a cliente',
                'descripcion': 'Un cliente mostró interés en nuestro nuevo producto pero no ha respondido desde la última reunión. Redacta un correo profesional y conciso para hacer un seguimiento, resaltando el beneficio clave del producto.',
                'respuesta_esperada': 'Asunto: Seguimiento: Información sobre nuestro nuevo [Nombre del Producto]\n\nEstimado/a [Nombre del Cliente],\n\nEspero que este correo lo encuentre bien. Quería hacer un seguimiento rápido de nuestra conversación anterior sobre [Nombre del Producto]. Desde nuestra reunión, hemos visto que este producto ha ayudado a otras empresas a [beneficio clave, ej: mejorar la eficiencia en un 20%].\n\n¿Habría algún momento la próxima semana que le viniera bien para una breve llamada y así poder resolver cualquier duda que pueda tener? Estoy seguro de que los beneficios de [Nombre del Producto] serían muy relevantes para [Empresa del Cliente].\n\nGracias de antemano por su tiempo.\n\nSaludos cordiales,\n[Tu Nombre]',
                'dificultad': 'Fácil'
            },
            {
                'nombre': 'Organizar una agenda de reunión semanal',
                'descripcion': 'Prepara una agenda detallada para la reunión de equipo semanal. Incluye los siguientes puntos: revisión de progresos de proyectos, desafíos actuales, próximos pasos y un espacio para "otros temas". La reunión durará 60 minutos.',
                'respuesta_esperada': 'Agenda de Reunión de Equipo Semanal - [Fecha]\n\nHora: [Hora de inicio] - [Hora de fin]\nUbicación: [Sala/Enlace de Videollamada]\n\n1.  **Revisión de Progresos (15 min)**\n    * Actualizaciones de Proyectos A, B, C.\n    * Logros de la semana.\n2.  **Desafíos Actuales y Obstáculos (20 min)**\n    * Identificación de problemas.\n    * Lluvia de ideas para soluciones.\n3.  **Próximos Pasos y Asignación de Tareas (15 min)**\n    * Definición de objetivos para la próxima semana.\n    * Asignación de responsabilidades.\n4.  **Otros Temas / Preguntas (10 min)**\n    * Espacio abierto para discusión de puntos no incluidos.',
                'dificultad': 'Normal'
            },
            {
                'nombre': 'Responder a una crítica negativa en redes sociales',
                'descripcion': 'Un cliente ha publicado una crítica pública muy negativa sobre nuestro servicio al cliente en Twitter/X, mencionando un problema que tuvo y su insatisfacción. Redacta una respuesta pública que sea profesional, empática y que invite a la resolución del problema fuera de la vista pública.',
                'respuesta_esperada': 'Lamentamos mucho escuchar sobre su experiencia, [Nombre de Usuario del Cliente]. Entendemos su frustración y nos tomamos sus comentarios muy en serio. Nos gustaría tener la oportunidad de investigar esto más a fondo y ayudarle a resolverlo. ¿Podría enviarnos un mensaje directo (DM) con más detalles sobre su caso y su información de contacto? Queremos asegurarnos de que reciba la atención que merece. Gracias por su paciencia.',
                'dificultad': 'Normal'
            },
            {
                'nombre': 'Preparar un resumen ejecutivo de un informe complejo',
                'descripcion': 'Has recibido un informe técnico de 20 páginas sobre la viabilidad de un nuevo proyecto. Tu tarea es extraer los puntos clave y preparar un resumen ejecutivo de no más de 1 párrafo para la dirección, que incluya el objetivo, las principales conclusiones y la recomendación final.',
                'respuesta_esperada': 'El informe de viabilidad del proyecto "[Nombre del Proyecto]" evalúa su potencial para [Objetivo del proyecto]. Las conclusiones principales indican que, si bien existe un alto potencial de [beneficio], también se identifican riesgos significativos relacionados con [riesgo principal]. Por lo tanto, se recomienda proceder con una fase piloto limitada para validar las suposiciones clave y mitigar los riesgos antes de una inversión a gran escala, asegurando así una toma de decisión basada en datos más concretos.',
                'dificultad': 'Difícil'
            },
            {
                'nombre': 'Planificar una campaña de marketing básica',
                'descripcion': 'Desarrolla un plan de campaña de marketing básico para lanzar un nuevo servicio de consultoría online. Define el público objetivo, los canales principales (menciona al menos 2) y un mensaje clave.',
                'respuesta_esperada': 'Plan de Campaña: Lanzamiento Servicio de Consultoría Online\n\nPúblico Objetivo: Pequeñas y medianas empresas (PyMEs) y emprendedores que buscan optimizar su presencia digital y eficiencia operativa.\n\nCanales Principales:\n1.  **Redes Sociales (LinkedIn, Facebook):** Para contenido educativo, testimonios y anuncios segmentados.\n2.  **Email Marketing:** Creación de una lista de leads a través de un webinar gratuito o descarga de guía, seguida de una secuencia de correos informativos y de venta.\n\nMensaje Clave: "Transforma tu negocio online con nuestra consultoría experta: soluciones prácticas para crecimiento real."',
                'dificultad': 'Normal'
            },
            {
                'nombre': 'Escribir una disculpa por un error de facturación',
                'descripcion': 'Un cliente ha recibido una factura incorrecta con un cargo duplicado. Redacta un correo de disculpa que reconozca el error, explique las medidas tomadas para corregirlo y asegure al cliente que no volverá a ocurrir.',
                'respuesta_esperada': 'Asunto: Disculpa por error en su factura [Número de Factura]\n\nEstimado/a [Nombre del Cliente],\n\nLe escribimos para ofrecerle nuestras más sinceras disculpas por el error de facturación que ha experimentado con su factura [Número de Factura], donde se duplicó el cargo por [Mencionar el concepto duplicado].\n\nHemos corregido este error inmediatamente y ya hemos procesado el ajuste necesario para revertir el cargo duplicado. Debería ver la corrección reflejada en su estado de cuenta en los próximos [Número] días hábiles.\n\nHemos revisado nuestros procesos internos para asegurar que este tipo de error no se repita. Valoramos mucho su confianza y lamentamos cualquier inconveniente que esto le haya podido causar.\n\nSi tiene alguna pregunta, no dude en contactarnos.\n\nAtentamente,\n[Tu Nombre/Nombre de la Empresa]',
                'dificultad': 'Fácil'
            },
            {
                'nombre': 'Preparar un informe de gastos mensual',
                'descripcion': 'Organiza los siguientes gastos mensuales en un formato claro para un informe: Viajes de negocios: $350. Material de oficina: $80. Software de suscripción: $120. Comidas con clientes: $150. Transportes: $50. Calcula el total.',
                'respuesta_esperada': 'Informe de Gastos Mensual - [Mes/Año]\n\nDetalle de Gastos:\n* **Viajes de negocios:** $350.00\n* **Material de oficina:** $80.00\n* **Software de suscripción:** $120.00\n* **Comidas con clientes:** $150.00\n* **Transportes:** $50.00\n\n**Total de Gastos:** $750.00\n\nNotas adicionales: [Espacio para cualquier comentario relevante, ej: "Los gastos de viaje incluyen el vuelo a la conferencia de la industria."]',
                'dificultad': 'Fácil'
            },
            {
                'nombre': 'Diseñar un proceso simple de onboarding para nuevos empleados',
                'descripcion': 'Crea un esquema de los pasos clave para el proceso de integración de un nuevo empleado en los primeros 3 días. Incluye aspectos como documentación, presentación al equipo, configuración de herramientas y primera tarea.',
                'respuesta_esperada': 'Proceso de Onboarding de Nuevo Empleado (Primeros 3 Días)\n\n**Día 1: Bienvenida y Administrativo**\n1.  **Documentación y RH:** Firmar contrato, completar formularios de RRHH.\n2.  **Orientación:** Presentación general de la empresa, cultura y políticas.\n3.  **Presentación al Equipo:** Saludos individuales y presentación formal.\n4.  **Configuración de Herramientas:** Acceso a cuentas, correo electrónico, software esencial.\n5.  **Tour de las Instalaciones.**\n\n**Día 2: Inmersión y Aprendizaje**\n1.  **Reunión con el Mentor/Supervisor:** Revisión de roles, expectativas y objetivos iniciales.\n2.  **Capacitación de Herramientas Específicas:** Sesiones de formación sobre software o sistemas clave.\n3.  **Lectura de Material Relevante:** Documentación del proyecto, manuales.\n4.  **Almuerzo con el equipo.**\n\n**Día 3: Primeras Contribuciones y Preguntas**\n1.  **Asignación de una Primera Tarea Sencilla:** Que permita aplicar conocimientos y familiarizarse.\n2.  **Sesión de Preguntas y Respuestas:** Espacio para resolver dudas acumuladas.\n3.  **Feedback Inicial:** Conversación informal sobre cómo se siente el nuevo empleado.',
                'dificultad': 'Difícil'
            },
            {
                'nombre': 'Comunicar un cambio menor en la política de la empresa',
                'descripcion': 'La empresa ha decidido implementar un cambio menor: a partir del próximo mes, el uso de las impresoras debe limitarse a documentos esenciales para reducir el consumo de papel. Redacta un anuncio interno breve y claro para todos los empleados.',
                'respuesta_esperada': 'Asunto: Recordatorio Importante: Política de Uso de Impresoras\n\nEstimados/as Empleados/as,\n\nA partir del [Fecha de inicio, ej: 1 de agosto], implementaremos un cambio menor en nuestra política de uso de impresoras con el fin de reducir nuestro consumo de papel y fomentar prácticas más sostenibles.\n\nLes pedimos amablemente que, en lo posible, limiten la impresión a documentos estrictamente esenciales. Les animamos a utilizar formatos digitales siempre que sea viable.\n\nEste pequeño cambio contribuirá significativamente a nuestros objetivos de sostenibilidad y al cuidado de los recursos. Agradecemos de antemano su comprensión y colaboración.\n\nSaludos cordiales,\n[Tu Departamento/Dirección]',
                'dificultad': 'Fácil'
            },
            {
                'nombre': 'Analizar datos de ventas básicas y recomendar acción',
                'descripcion': 'Tienes los siguientes datos de ventas para el último trimestre: Producto A: $15,000, Producto B: $25,000, Producto C: $8,000. El Producto B es el nuevo lanzamiento. Analiza estos datos y haz una recomendación simple para el próximo trimestre.',
                'respuesta_esperada': 'Análisis de Ventas del Último Trimestre:\n\n* **Producto A:** $15,000\n* **Producto B (Nuevo Lanzamiento):** $25,000\n* **Producto C:** $8,000\n\nEl Producto B, siendo un nuevo lanzamiento, ha demostrado ser el más exitoso en ventas este trimestre, lo cual es muy positivo. El Producto A mantiene un buen desempeño, mientras que el Producto C muestra el rendimiento más bajo.\n\n**Recomendación para el Próximo Trimestre:**\nSe recomienda enfocar los esfuerzos de marketing y ventas en el Producto B para capitalizar su éxito inicial y explorar su potencial máximo. Para el Producto C, se sugiere una revisión de su estrategia de mercado o la consideración de ofertas promocionales para impulsar sus ventas.',
                'dificultad': 'Difícil'
            },
        ]

        self.stdout.write(self.style.NOTICE(f"Intentando crear {len(tareas_a_crear)} tareas de ejemplo..."))

        for tarea_data in tareas_a_crear:
            # Comprobamos si ya existe una tarea con el mismo nombre para evitar duplicados
            if not TareaSimulacion.objects.filter(nombre=tarea_data['nombre']).exists():
                TareaSimulacion.objects.create(**tarea_data)
                self.stdout.write(self.style.SUCCESS(f"Tarea '{tarea_data['nombre']}' creada con éxito."))
            else:
                self.stdout.write(self.style.WARNING(f"Tarea '{tarea_data['nombre']}' ya existe. Saltando."))

        self.stdout.write(self.style.SUCCESS('Proceso de creación de tareas de ejemplo finalizado.'))
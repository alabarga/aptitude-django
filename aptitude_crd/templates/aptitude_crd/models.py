from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from django.dispatch import receiver
from django.urls import reverse

_SEX = (
	(1, _("Hombre")),
	(2, _("Mujer")),
	)

_ASA = (
	(1, _("Hombre")),
	(2, _("Mujer")),
	)

_NO_YES = (
	(0, _("No")),
	(1, _("Sí")),
	)

_NO_YES_U = (
	(0, _("No")),
	(1, _("Sí")),
	(-1, _("Desconocido")),    
	)

# - Nombre
# - Apellidos
# - DNI paciente
# - Dirección
# - Identificador
# - Teléfono
# - Email
# - Consentimiento informado
# - Campos de interés:
#         ◦ Deterioro cognitivo
#         ◦ Fragilidad
#         ◦ Cáncer
#         ◦ Incontinencia de orina y/o heces
#         ◦ Caídas
#         ◦ Diabetes
#         ◦ úlceras por presión
#         ◦ problemas cardiovasculares
#         ◦ problemas respiratorios
#         ◦ problemas renales
#         ◦ problemas digestivos
#         ◦ problemas endocrinos
#         ◦ problemas alimentarios y dentales
#         ◦ problemas reumatológicos
#         ◦ problemas hematológicos
#         ◦ problemas psiquiátricos
#         ◦ problemas de movilidad
#         ◦ problemas neurológicos
#         ◦ déficits sensoriales
#         ◦ polifarmacia
#         ◦ estilos de vida saludables
#         ◦ otros

class Tema(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo   

class Registro(models.Model):
    
    nombre = models.CharField(verbose_name = _("Nombre"), max_length=64)
    apellidos = models.CharField(verbose_name = _("Apellidos"), max_length=64)
    email = models.EmailField(verbose_name = _("Correo electrónico"), max_length=50, blank= True, null = True)

    dni = models.CharField(verbose_name = _("DNI"), max_length=10, blank= True, null = True)
    direccion = models.CharField(verbose_name = _("Dirección"), max_length=255, blank= True, null = True)
    ciudad = models.CharField(verbose_name = _("Ciudad"), max_length=255, blank= True, null = True)
    pais = models.CharField(verbose_name = _("País"), max_length=255, blank= True, null = True)
    fecha_nacimiento = models.DateField(verbose_name = _("Fecha de nacimiento"), blank= True, null = True)
    sexo = models.IntegerField(verbose_name = _("Sexo"), choices = _SEX, blank= True, null = True)        
    telefono = models.CharField(verbose_name = _("Teléfono"), max_length=9, blank= True, null = True)
    consentimiento = models.FileField(verbose_name = _("Consentimiento informado"), blank= True, null = True)

    temas = models.ManyToManyField(Tema, verbose_name = _("Campos de interés"))

    @property
    def edad(self):
        today = date.today() 
        age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) <  (self.fecha_nacimiento.month, self.fecha_nacimiento.day)) 
  
        return age 

    @property
    def rango_edad(self):

        rangos = { '0-15': (0,15),
                   '16-35': (16,35),
                   '36-50':(36, 50),
                   '51-65': (51,65),
                   '66-80': (66,80),
                   '80+':(80,120)     
                }

        edad = self.edad
        for rango, valores in rangos.items():
            if edad >= valores[0] and edad <= valores[1]:
                return rango
  
    

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)

# Código del paciente (numérica).
# Fecha de nacimiento (día/mes/año).
# Sexo (categórica)
# Acceso a Internet (sí/no).
# Nivel de estudios: No escolarizado/ estudios primarios/estudios de secundaria/bachillerato/ universitario/ desconocido.

# Captación del paciente: médico general/especialista/farmacéutico/médico de la mutua/ familiar/ ayuntamiento/investigador/estación termal/convocatoria anual/otro.
# Frecuencia de visitas médicas: < 3meses/ 3-12 meses/ >12 meses/ sin seguimiento/ desconocido.

# Convivencia: solo/ con familia/ con pareja/ otro/ desconocido.
# Ayuda domiciliaria: ninguna/ comida/ tareas domésticas/ enfermero

# Evaluador: enfermera especialista en geriatria/ enfermera otros/ médico general/equipo multidisciplinar/médico residente/médico general/otros.
# Motivo de evaluación: impresión de fragilidad/ queja cognitiva/ desconocido

_NIVEL_ESTUDIOS  = (
	(0, _("No escolarizado")),
	(1, _("Estudios primarios")),
	(2, _("Estudios de secundaria")),   
	(3, _("Bachillerato")),
	(4, _("Estudios universitarios")),
	(-1, _("Desconocido")),     
	)

_CAPTACION  = (
	(0, _("médico general")),
	(1, _("especialista")),
	(2, _("farmacéutico")),   
	(3, _("médico de la mutua")),
	(4, _("familiar")),
	(5, _("Ayuntamiento")), 
	(6, _("investigador")),
	(7, _("estación termal")),
	(8, _("convocatoria anual")),   
	(9, _("otro")),           
	)

_MOTIVO = (
    (0, _("Impresión de fragilidad")),
    (1, _("queja cognitiva")),
	(2, _("seguimiento")),   
    (-1, _("desconocido")),   
    )

_PROFESIONAL = (
    (0, _("enfermera especialista en geriatria")),
	(1, _("enfermera otros")),
	(2, _("médico general")),   
    (3, _("equipo multidisciplinar")),  
	(4, _("médico residente")),
	(5, _("otros")),
    )  

_COMP_TYPES = (
    ('TEXT', _("Texto")),
    ('NUM', _("Numérico")),
    ('VAL', _("Lista_Valor")), 
	('LIST', _("Lista")),   
    ('CALC', _("Calculado")),  
    )  

_OP_TYPES = (
    ('TEXT', _("Texto")),
    ('NUM', _("Numérico")), 
    ) 

class Cuestionario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(verbose_name = _("Tipo"), max_length=10, choices= _COMP_TYPES)
    valor_defecto = models.CharField(verbose_name = _("Valor por defecto"), max_length=100, blank= True, null = True)
    lista = models.CharField(verbose_name = _("Lista"), max_length=100, blank= True, null = True)
    funcion = models.CharField(verbose_name = _("Funcion"), max_length=100, blank= True, null = True)

    def __str__(self):
        return self.nombre  

class Opcion(models.Model):
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(verbose_name = _("Tipo"), max_length=10, choices= _OP_TYPES)
    valor = models.CharField(verbose_name = _("Valor"), max_length=10)

    def __str__(self):
        return self.nombre 

    def value(self):
        return eval(self.valor)

class Paciente(models.Model):
    
    codigo = models.CharField(verbose_name = _("Codigo"), max_length=64)
    fecha_nacimiento = models.DateField(verbose_name = _("Fecha de nacimiento"), blank= True, null = True)
    sexo = models.IntegerField(verbose_name = _("Sexo"), choices = _SEX, blank= True, null = True)     

    internet = models.IntegerField(verbose_name = _("Acceso a internet"), choices = _NO_YES_U, blank= True, null = True) 
    nivel_estudios = models.IntegerField(verbose_name = _("Nivel de estudios"), choices = _NIVEL_ESTUDIOS, blank= True, null = True) 
    captacion = models.IntegerField(verbose_name = _("Captación del paciente"), choices = _CAPTACION, blank= True, null = True) 

    def __str__(self):
        return self.codigo  

class Visita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name = _("Fecha de la visita"), blank= True, null = True)

    motivo = models.IntegerField(verbose_name = _("Motivo de evaluación"), choices = _MOTIVO, blank= True, null = True) 
    evaluador = models.IntegerField(verbose_name = _("Evaluador"), choices = _PROFESIONAL, blank= True, null = True) 

    cuestionarios = models.ManyToManyField(Cuestionario)

    def add_cuestionarios(self):
        for cuestionario in self.cuestionarios.all():
            evaluacion = Evaluacion.objects.get_or_create(
                visita=self,
                cuestionario=cuestionario
            )

    def __str__(self):
        return "{} ({})".format(_MOTIVO[self.motivo][1], self.fecha)

@receiver(models.signals.post_save, sender=Visita)
def execute_after_save(sender, instance, created, *args, **kwargs):
    instance.add_cuestionarios()

class Evaluacion(models.Model):
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE, related_name='evaluaciones')
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.cuestionario.nombre 

    def get_absolute_url(self):
        return reverse('evaluacion', args=[self.id,])

    def add_preguntas(self):
        for componente in self.cuestionario.componentes.all():
            pregunta = Pregunta.objects.get_or_create(
                visita=self.visita,
                componente=componente,
            )

    class Meta:
        verbose_name_plural = "evaluaciones"


class Pregunta(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return str(self.componente)


    # nombre = models.CharField(verbose_name = _("Nombre"), max_length=64)
    # apellidos = models.CharField(verbose_name = _("Apellidos"), max_length=64)
    # email = models.EmailField(verbose_name = _("Correo electrónico"), max_length=9, blank= True, null = True)

    # dni = models.CharField(verbose_name = _("DNI"), max_length=9, blank= True, null = True)
    # direccion = models.CharField(verbose_name = _("Dirección"), max_length=255, blank= True, null = True)
    # fecha_nacimiento = models.DateField(verbose_name = _("Fecha de nacimiento"), blank= True, null = True)
    # sexo = models.IntegerField(verbose_name = _("Sexo"), choices = _SEX, blank= True, null = True)        
    # telefono = models.CharField(verbose_name = _("Teléfono"), max_length=9, blank= True, null = True)
    # consentimiento = models.FileField(verbose_name = _("Consentimiento informado"), blank= True, null = True)
    #intereses = 

# Captación del paciente: médico general/especialista/farmacéutico/médico de la mutua/ familiar/ ayuntamiento/investigador/estación termal/convocatoria anual/otro.
# Evaluador: enfermera especialista en geriatria/ enfermera otros/ médico general/equipo multidisciplinar/médico residente/médico general/otros.
# Motivo de evaluación: impresión de fragilidad/ queja cognitiva/ desconocido
# Frecuencia de visitas médicas: < 3meses/ 3-12 meses/ >12 meses/ sin seguimiento/ desconocido.
# Nivel de estudios: No escolarizado/ estudios primarios/estudios de secundaria/bachillerato/ universitario/ desconocido.
# Convivencia: solo/ con familia/ con pareja/ otro/ desconocido.
# Ayuda domiciliaria: ninguna/ comida/ tareas domésticas/ enfermeros/ quiropráctico/teleasistencia/ desconocido.
# Prestación económica por situación de dependencia: Si/No/desconocido.
# Medidas de protección jurídica: Sí/No/desconocido.
# No de patologías crónicas
# No de tratamientos habituales
# Cáncer en tratamiento actual: Sí/No/Desconocido

# class Patient(models.Model):

#     asa = models.IntegerField(verbose_name = "ASA", choices = _ASA , blank= True, null = True)
#     hypertension = models.IntegerField(verbose_name = "Hypertension", choices = _NO_YES, blank= True, null = True)
#     hb = models.FloatField(verbose_name = "HB (g/dL)", blank= True, null = True)
#     platelets = models.IntegerField(verbose_name = "Platelets (x10⁹/L)", blank= True, null = True)
#     """
#         Glucoses
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     moment = models.IntegerField(null=True)
#     glucose = models.DecimalField(max_digits=5, decimal_places=2)
#     insulin = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     comment = models.TextField()
#     date_glucoses = models.DateField()
#     hour_glucoses = models.TimeField()
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'Glucose'
#         verbose_name_plural = 'Glucoses'

#     def __str__(self):
#         return "Glucose: %s Insulin: %s (date: %s)" % (
#                                                 self.glucose,
#                                                 self.insulin,
#                                                 self.date_glucoses)
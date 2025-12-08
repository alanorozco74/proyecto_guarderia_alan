from django.db import models

# ===================
# TABLA 1: PADRE / MADRE
# ===================
class PadreMadre(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono_principal = models.CharField(max_length=20)
    telefono_alternativo = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    relacion_con_nino = models.CharField(max_length=50) # Padre, Madre, Tutor
    profesion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.relacion_con_nino})"

# ===================
# TABLA 2: PERSONAL GUARDERÍA
# ===================
class PersonalGuarderia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20)
    certificaciones = models.TextField(blank=True, null=True)
    turno = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Personal de Guardería"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

# ===================
# TABLA 3: GRUPO DE NIÑOS
# ===================
class GrupoNinos(models.Model):
    nombre_grupo = models.CharField(max_length=50)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    num_ninos_actual = models.IntegerField(default=0)
    capacidad_maxima = models.IntegerField()
    descripcion_actividades = models.TextField(blank=True, null=True)
    
    personal_cargo = models.ForeignKey(
        PersonalGuarderia, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="grupos"
    )

    class Meta:
        verbose_name_plural = "Grupos de Niños"

    def __str__(self):
        return self.nombre_grupo

# ===================
# TABLA 4: NIÑO
# ===================
class Nino(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    alergias = models.TextField(blank=True, null=True)
    necesidades_especiales = models.TextField(blank=True, null=True)
    fecha_inscripcion = models.DateField()

    padre_principal = models.ForeignKey(
        PadreMadre,
        on_delete=models.CASCADE,
        related_name="hijos"
    )
    
    grupo_asignado = models.ForeignKey(
        GrupoNinos,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ninos"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===================
# TABLA 5: ACTIVIDAD GUARDERÍA
# ===================
class ActividadGuarderia(models.Model):
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=100) # Ej: "10:00 - 11:00"
    duracion_minutos = models.IntegerField()
    material_requerido = models.TextField(blank=True, null=True)
    es_obligatoria = models.BooleanField(default=True)

    grupo = models.ForeignKey(
        GrupoNinos,
        on_delete=models.CASCADE,
        related_name="actividades"
    )

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.nombre_actividad} ({self.grupo.nombre_grupo})"

# ===================
# TABLA 6: ASISTENCIA NIÑO
# ===================
class AsistenciaNino(models.Model):
    fecha_asistencia = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)
    estuvo_enfermo = models.BooleanField(default=False)
    notas_dia = models.TextField(blank=True, null=True)

    nino = models.ForeignKey(
        Nino,
        on_delete=models.CASCADE,
        related_name="asistencias"
    )
    
    personal_registro = models.ForeignKey(
        PersonalGuarderia,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return f"Asistencia: {self.nino} - {self.fecha_asistencia}"

# ===================
# TABLA 7: PAGO MENSUALIDAD
# ===================
class PagoMensualidad(models.Model):
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=100) # Ej: "Marzo 2025"
    metodo_pago = models.CharField(max_length=50)
    mes_correspondiente = models.DateField() # Guardar el primer día del mes pagado
    estado_pago = models.CharField(max_length=50, default='Pagado')
    fecha_vencimiento = models.DateField()

    nino = models.ForeignKey(
        Nino,
        on_delete=models.CASCADE,
        related_name="pagos"
    )

    class Meta:
        verbose_name_plural = "Pagos Mensualidades"

    def __str__(self):
        return f"Pago {self.concepto} - {self.nino}"
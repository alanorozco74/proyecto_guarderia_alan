from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    PadreMadre, PersonalGuarderia, GrupoNinos, Nino, 
    ActividadGuarderia, AsistenciaNino, PagoMensualidad
)

def inicio_guarderia(request):
    return render(request, 'inicio.html')

# --- PADRES ---
def ver_padres(request):
    padres = PadreMadre.objects.all()
    return render(request, 'padre/ver_padres.html', {'padres': padres})

def agregar_padre(request):
    if request.method == 'POST':
        PadreMadre.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono_principal=request.POST.get('telefono_principal'),
            telefono_alternativo=request.POST.get('telefono_alternativo'),
            direccion=request.POST.get('direccion'),
            dni=request.POST.get('dni'),
            relacion_con_nino=request.POST.get('relacion_con_nino'),
            profesion=request.POST.get('profesion')
        )
        return redirect('ver_padres')
    return render(request, 'padre/agregar_padre.html')

def actualizar_padre(request, id):
    padre = get_object_or_404(PadreMadre, id=id)
    return render(request, 'padre/actualizar_padre.html', {'padre': padre})

def realizar_actualizacion_padre(request, id):
    padre = get_object_or_404(PadreMadre, id=id)
    if request.method == 'POST':
        padre.nombre = request.POST.get('nombre')
        padre.apellido = request.POST.get('apellido')
        padre.email = request.POST.get('email')
        padre.telefono_principal = request.POST.get('telefono_principal')
        padre.telefono_alternativo = request.POST.get('telefono_alternativo')
        padre.direccion = request.POST.get('direccion')
        padre.dni = request.POST.get('dni')
        padre.relacion_con_nino = request.POST.get('relacion_con_nino')
        padre.profesion = request.POST.get('profesion')
        padre.save()
        return redirect('ver_padres')
    return render(request, 'padre/actualizar_padre.html', {'padre': padre})

def borrar_padre(request, id):
    padre = get_object_or_404(PadreMadre, id=id)
    if request.method == 'POST':
        padre.delete()
        return redirect('ver_padres')
    return render(request, 'padre/borrar_padre.html', {'padre': padre})

# --- PERSONAL ---
def ver_personal(request):
    personal = PersonalGuarderia.objects.all()
    return render(request, 'personal/ver_personal.html', {'personal': personal})

def agregar_personal(request):
    if request.method == 'POST':
        PersonalGuarderia.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            cargo=request.POST.get('cargo'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            fecha_contratacion=request.POST.get('fecha_contratacion'),
            salario=request.POST.get('salario'),
            dni=request.POST.get('dni'),
            certificaciones=request.POST.get('certificaciones'),
            turno=request.POST.get('turno')
        )
        return redirect('ver_personal')
    return render(request, 'personal/agregar_personal.html')

def actualizar_personal(request, id):
    p = get_object_or_404(PersonalGuarderia, id=id)
    return render(request, 'personal/actualizar_personal.html', {'p': p})

def realizar_actualizacion_personal(request, id):
    p = get_object_or_404(PersonalGuarderia, id=id)
    if request.method == 'POST':
        p.nombre = request.POST.get('nombre')
        p.apellido = request.POST.get('apellido')
        p.cargo = request.POST.get('cargo')
        p.email = request.POST.get('email')
        p.telefono = request.POST.get('telefono')
        p.fecha_contratacion = request.POST.get('fecha_contratacion')
        p.salario = request.POST.get('salario')
        p.dni = request.POST.get('dni')
        p.certificaciones = request.POST.get('certificaciones')
        p.turno = request.POST.get('turno')
        p.save()
        return redirect('ver_personal')
    return render(request, 'personal/actualizar_personal.html', {'p': p})

def borrar_personal(request, id):
    p = get_object_or_404(PersonalGuarderia, id=id)
    if request.method == 'POST':
        p.delete()
        return redirect('ver_personal')
    return render(request, 'personal/borrar_personal.html', {'p': p})

# --- GRUPOS ---
def ver_grupos(request):
    grupos = GrupoNinos.objects.all()
    return render(request, 'grupo/ver_grupos.html', {'grupos': grupos})

def agregar_grupo(request):
    personal = PersonalGuarderia.objects.all()
    if request.method == 'POST':
        p_obj = get_object_or_404(PersonalGuarderia, id=request.POST.get('personal_cargo'))
        GrupoNinos.objects.create(
            nombre_grupo=request.POST.get('nombre_grupo'),
            edad_minima=request.POST.get('edad_minima'),
            edad_maxima=request.POST.get('edad_maxima'),
            num_ninos_actual=request.POST.get('num_ninos_actual'),
            capacidad_maxima=request.POST.get('capacidad_maxima'),
            descripcion_actividades=request.POST.get('descripcion_actividades'),
            personal_cargo=p_obj
        )
        return redirect('ver_grupos')
    return render(request, 'grupo/agregar_grupo.html', {'personal': personal})

def actualizar_grupo(request, id):
    grupo = get_object_or_404(GrupoNinos, id=id)
    personal = PersonalGuarderia.objects.all()
    return render(request, 'grupo/actualizar_grupo.html', {'grupo': grupo, 'personal': personal})

def realizar_actualizacion_grupo(request, id):
    grupo = get_object_or_404(GrupoNinos, id=id)
    if request.method == 'POST':
        grupo.nombre_grupo = request.POST.get('nombre_grupo')
        grupo.edad_minima = request.POST.get('edad_minima')
        grupo.edad_maxima = request.POST.get('edad_maxima')
        grupo.num_ninos_actual = request.POST.get('num_ninos_actual')
        grupo.capacidad_maxima = request.POST.get('capacidad_maxima')
        grupo.descripcion_actividades = request.POST.get('descripcion_actividades')
        grupo.personal_cargo = get_object_or_404(PersonalGuarderia, id=request.POST.get('personal_cargo'))
        grupo.save()
        return redirect('ver_grupos')
    return redirect('ver_grupos')

def borrar_grupo(request, id):
    grupo = get_object_or_404(GrupoNinos, id=id)
    if request.method == 'POST':
        grupo.delete()
        return redirect('ver_grupos')
    return render(request, 'grupo/borrar_grupo.html', {'grupo': grupo})

# --- NIÑOS ---
def ver_ninos(request):
    ninos = Nino.objects.all()
    return render(request, 'nino/ver_ninos.html', {'ninos': ninos})

def agregar_nino(request):
    padres = PadreMadre.objects.all()
    grupos = GrupoNinos.objects.all()
    if request.method == 'POST':
        padre_obj = get_object_or_404(PadreMadre, id=request.POST.get('padre_principal'))
        grupo_obj = get_object_or_404(GrupoNinos, id=request.POST.get('grupo_asignado'))
        Nino.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            genero=request.POST.get('genero'),
            alergias=request.POST.get('alergias'),
            necesidades_especiales=request.POST.get('necesidades_especiales'),
            fecha_inscripcion=request.POST.get('fecha_inscripcion'),
            padre_principal=padre_obj,
            grupo_asignado=grupo_obj
        )
        return redirect('ver_ninos')
    return render(request, 'nino/agregar_nino.html', {'padres': padres, 'grupos': grupos})

def actualizar_nino(request, id):
    nino = get_object_or_404(Nino, id=id)
    padres = PadreMadre.objects.all()
    grupos = GrupoNinos.objects.all()
    return render(request, 'nino/actualizar_nino.html', {'nino': nino, 'padres': padres, 'grupos': grupos})

def realizar_actualizacion_nino(request, id):
    nino = get_object_or_404(Nino, id=id)
    if request.method == 'POST':
        nino.nombre = request.POST.get('nombre')
        nino.apellido = request.POST.get('apellido')
        nino.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        nino.genero = request.POST.get('genero')
        nino.alergias = request.POST.get('alergias')
        nino.necesidades_especiales = request.POST.get('necesidades_especiales')
        nino.fecha_inscripcion = request.POST.get('fecha_inscripcion')
        nino.padre_principal = get_object_or_404(PadreMadre, id=request.POST.get('padre_principal'))
        nino.grupo_asignado = get_object_or_404(GrupoNinos, id=request.POST.get('grupo_asignado'))
        nino.save()
        return redirect('ver_ninos')
    return redirect('ver_ninos')

def borrar_nino(request, id):
    nino = get_object_or_404(Nino, id=id)
    if request.method == 'POST':
        nino.delete()
        return redirect('ver_ninos')
    return render(request, 'nino/borrar_nino.html', {'nino': nino})

# --- ACTIVIDADES ---
def ver_actividades(request):
    actividades = ActividadGuarderia.objects.all()
    return render(request, 'actividad/ver_actividades.html', {'actividades': actividades})

def agregar_actividad(request):
    grupos = GrupoNinos.objects.all()
    if request.method == 'POST':
        grupo_obj = get_object_or_404(GrupoNinos, id=request.POST.get('grupo'))
        ActividadGuarderia.objects.create(
            nombre_actividad=request.POST.get('nombre_actividad'),
            descripcion=request.POST.get('descripcion'),
            horario=request.POST.get('horario'),
            duracion_minutos=request.POST.get('duracion_minutos'),
            material_requerido=request.POST.get('material_requerido'),
            es_obligatoria=request.POST.get('es_obligatoria') == 'on',
            grupo=grupo_obj
        )
        return redirect('ver_actividades')
    return render(request, 'actividad/agregar_actividad.html', {'grupos': grupos})

def actualizar_actividad(request, id):
    act = get_object_or_404(ActividadGuarderia, id=id)
    grupos = GrupoNinos.objects.all()
    return render(request, 'actividad/actualizar_actividad.html', {'act': act, 'grupos': grupos})

def realizar_actualizacion_actividad(request, id):
    act = get_object_or_404(ActividadGuarderia, id=id)
    if request.method == 'POST':
        act.nombre_actividad = request.POST.get('nombre_actividad')
        act.descripcion = request.POST.get('descripcion')
        act.horario = request.POST.get('horario')
        act.duracion_minutos = request.POST.get('duracion_minutos')
        act.material_requerido = request.POST.get('material_requerido')
        act.es_obligatoria = request.POST.get('es_obligatoria') == 'on'
        act.grupo = get_object_or_404(GrupoNinos, id=request.POST.get('grupo'))
        act.save()
        return redirect('ver_actividades')
    return redirect('ver_actividades')

def borrar_actividad(request, id):
    act = get_object_or_404(ActividadGuarderia, id=id)
    if request.method == 'POST':
        act.delete()
        return redirect('ver_actividades')
    return render(request, 'actividad/borrar_actividad.html', {'act': act})

# --- ASISTENCIAS ---
def ver_asistencias(request):
    asistencias = AsistenciaNino.objects.all()
    return render(request, 'asistencia/ver_asistencias.html', {'asistencias': asistencias})

def agregar_asistencia(request):
    ninos = Nino.objects.all()
    personal = PersonalGuarderia.objects.all()
    if request.method == 'POST':
        nino_obj = get_object_or_404(Nino, id=request.POST.get('nino'))
        p_obj = get_object_or_404(PersonalGuarderia, id=request.POST.get('personal_registro'))
        AsistenciaNino.objects.create(
            fecha_asistencia=request.POST.get('fecha_asistencia'),
            hora_entrada=request.POST.get('hora_entrada'),
            hora_salida=request.POST.get('hora_salida') or None,
            estuvo_enfermo=request.POST.get('estuvo_enfermo') == 'on',
            notas_dia=request.POST.get('notas_dia'),
            nino=nino_obj,
            personal_registro=p_obj
        )
        return redirect('ver_asistencias')
    return render(request, 'asistencia/agregar_asistencia.html', {'ninos': ninos, 'personal': personal})

def actualizar_asistencia(request, id):
    a = get_object_or_404(AsistenciaNino, id=id)
    ninos = Nino.objects.all()
    personal = PersonalGuarderia.objects.all()
    return render(request, 'asistencia/actualizar_asistencia.html', {'a': a, 'ninos': ninos, 'personal': personal})

def realizar_actualizacion_asistencia(request, id):
    a = get_object_or_404(AsistenciaNino, id=id)
    if request.method == 'POST':
        a.fecha_asistencia = request.POST.get('fecha_asistencia')
        a.hora_entrada = request.POST.get('hora_entrada')
        a.hora_salida = request.POST.get('hora_salida') or None
        a.estuvo_enfermo = request.POST.get('estuvo_enfermo') == 'on'
        a.notas_dia = request.POST.get('notas_dia')
        a.nino = get_object_or_404(Nino, id=request.POST.get('nino'))
        a.personal_registro = get_object_or_404(PersonalGuarderia, id=request.POST.get('personal_registro'))
        a.save()
        return redirect('ver_asistencias')
    return redirect('ver_asistencias')

def borrar_asistencia(request, id):
    a = get_object_or_404(AsistenciaNino, id=id)
    if request.method == 'POST':
        a.delete()
        return redirect('ver_asistencias')
    return render(request, 'asistencia/borrar_asistencia.html', {'a': a})

# --- PAGOS ---
def ver_pagos(request):
    pagos = PagoMensualidad.objects.all().order_by('-fecha_pago')
    return render(request, 'pago/ver_pagos.html', {'pagos': pagos})

def agregar_pago(request):
    ninos = Nino.objects.all()
    if request.method == 'POST':
        nino_obj = get_object_or_404(Nino, id=request.POST.get('nino'))
        PagoMensualidad.objects.create(
            monto_pagado=request.POST.get('monto_pagado'),
            concepto=request.POST.get('concepto'),
            metodo_pago=request.POST.get('metodo_pago'),
            mes_correspondiente=request.POST.get('mes_correspondiente'),
            estado_pago=request.POST.get('estado_pago'),
            fecha_vencimiento=request.POST.get('fecha_vencimiento'),
            nino=nino_obj
        )
        return redirect('ver_pagos')
    return render(request, 'pago/agregar_pago.html', {'ninos': ninos})

def actualizar_pago(request, id):
    pago = get_object_or_404(PagoMensualidad, id=id)
    ninos = Nino.objects.all()
    return render(request, 'pago/actualizar_pago.html', {'pago': pago, 'ninos': ninos})

def realizar_actualizacion_pago(request, id):
    pago = get_object_or_404(PagoMensualidad, id=id)
    if request.method == 'POST':
        pago.monto_pagado = request.POST.get('monto_pagado')
        pago.concepto = request.POST.get('concepto')
        pago.metodo_pago = request.POST.get('metodo_pago')
        pago.mes_correspondiente = request.POST.get('mes_correspondiente')
        pago.estado_pago = request.POST.get('estado_pago')
        pago.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        pago.nino = get_object_or_404(Nino, id=request.POST.get('nino'))
        pago.save()
        return redirect('ver_pagos')
    return redirect('ver_pagos')

def borrar_pago(request, id):
    pago = get_object_or_404(PagoMensualidad, id=id)
    if request.method == 'POST':
        pago.delete()
        return redirect('ver_pagos')
    return render(request, 'pago/borrar_pago.html', {'pago': pago})
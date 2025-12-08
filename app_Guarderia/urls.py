from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_guarderia, name='inicio_guarderia'),

    # Rutas Padres
    path('padres/', views.ver_padres, name='ver_padres'),
    path('padres/agregar/', views.agregar_padre, name='agregar_padre'),
    path('padres/actualizar/<int:id>/', views.actualizar_padre, name='actualizar_padre'),
    path('padres/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_padre, name='realizar_actualizacion_padre'),
    path('padres/borrar/<int:id>/', views.borrar_padre, name='borrar_padre'),

    # Rutas Personal
    path('personal/', views.ver_personal, name='ver_personal'),
    path('personal/agregar/', views.agregar_personal, name='agregar_personal'),
    path('personal/actualizar/<int:id>/', views.actualizar_personal, name='actualizar_personal'),
    path('personal/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_personal, name='realizar_actualizacion_personal'),
    path('personal/borrar/<int:id>/', views.borrar_personal, name='borrar_personal'),

    # Rutas Grupos
    path('grupos/', views.ver_grupos, name='ver_grupos'),
    path('grupos/agregar/', views.agregar_grupo, name='agregar_grupo'),
    path('grupos/actualizar/<int:id>/', views.actualizar_grupo, name='actualizar_grupo'),
    path('grupos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_grupo, name='realizar_actualizacion_grupo'),
    path('grupos/borrar/<int:id>/', views.borrar_grupo, name='borrar_grupo'),

    # Rutas Niños
    path('ninos/', views.ver_ninos, name='ver_ninos'),
    path('ninos/agregar/', views.agregar_nino, name='agregar_nino'),
    path('ninos/actualizar/<int:id>/', views.actualizar_nino, name='actualizar_nino'),
    path('ninos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_nino, name='realizar_actualizacion_nino'),
    path('ninos/borrar/<int:id>/', views.borrar_nino, name='borrar_nino'),

    # Rutas Actividades
    path('actividades/', views.ver_actividades, name='ver_actividades'),
    path('actividades/agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('actividades/actualizar/<int:id>/', views.actualizar_actividad, name='actualizar_actividad'),
    path('actividades/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_actividad, name='realizar_actualizacion_actividad'),
    path('actividades/borrar/<int:id>/', views.borrar_actividad, name='borrar_actividad'),

    # Rutas Asistencias
    path('asistencias/', views.ver_asistencias, name='ver_asistencias'),
    path('asistencias/agregar/', views.agregar_asistencia, name='agregar_asistencia'),
    path('asistencias/actualizar/<int:id>/', views.actualizar_asistencia, name='actualizar_asistencia'),
    path('asistencias/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_asistencia, name='realizar_actualizacion_asistencia'),
    path('asistencias/borrar/<int:id>/', views.borrar_asistencia, name='borrar_asistencia'),

    # Rutas Pagos
    path('pagos/', views.ver_pagos, name='ver_pagos'),
    path('pagos/agregar/', views.agregar_pago, name='agregar_pago'),
    path('pagos/actualizar/<int:id>/', views.actualizar_pago, name='actualizar_pago'),
    path('pagos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_pago, name='realizar_actualizacion_pago'),
    path('pagos/borrar/<int:id>/', views.borrar_pago, name='borrar_pago'),
]
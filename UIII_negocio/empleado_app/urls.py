from django.urls import path 
from empleado_app import views

urlpatterns = [
    path("",views.inicio_vista, name="inicio_vista"),
    path("registrarEmpleado/",views.registrarMateria,name="registrarMateria"),
    path("seleccionarEmpleado/<codigo>",views.seleccionarMateria,name="seleccionarMateria"),
    path("editarEmpleado/",views.editarMateria,name="editarMateria"),
    path("borrarEmpleado/<codigo>",views.borrarMateria,name="borrarMateria")
]
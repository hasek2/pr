from django.urls import path
from .views import home, agregar_juego, editar_juego, borrar_juego

urlpatterns = [
    path('', home, name="home"),
    path('agregar-juego/', agregar_juego, name="agregar_juego" ),
    path('editar-juego/<id>/', editar_juego, name="editar_juego" ),
    path('borrar-juego/<id>/', borrar_juego, name="borrar_juego" ),
]
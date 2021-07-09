from django.urls import path
from rest_api.views import lista_juego, detalle_juego
from rest_api.viewsLogin import login


urlpatterns = [
    path('lista-juego/', lista_juego, name="lista_juego"),
    path('detalle-juego/<id>', detalle_juego, name="detalle_juego"),
    path('login/', login, name="login"),
]
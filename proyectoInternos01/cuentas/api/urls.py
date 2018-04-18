from django.conf.urls import url
from django.urls import path, include
#from rest_framework import routers



from .views import (
    UsuarioCrearAPI,
    UserViewAPI,
    UsuarioListarAPI,
    UsuarioDetalleAPI
)
# from . import views
#router = routers.DefaultRouter()
#router.register('',views.UserView)



urlpatterns = [
    #url('',include(router.urls)),

    url(r'^$', UsuarioListarAPI.as_view(), name='listar'),
    url(r'^registrar/$', UsuarioCrearAPI.as_view(), name='registrar'),
    url(r'(?P<id>\d+)/', UsuarioDetalleAPI.as_view(), name = 'detalle')
    
]

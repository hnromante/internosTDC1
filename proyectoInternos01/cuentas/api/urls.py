from django.conf.urls import url
from django.urls import path, include

#TOKEN AUTH ENDPOINT
from rest_framework.authtoken.views import obtain_auth_token



from .views import (
    UsuarioCrearAPIView,
    UserAPIViewset,
    UsuarioListarAPIView,
    UsuarioDetalleByIdAPIView,
    UsuarioDetalleByEmailAPIView,
    UsuarioEditarAPIView,
    UsuarioEliminarAPIView,
)
urlpatterns = [
    #url('',include(router.urls)),
    url(r'^$', UsuarioListarAPIView.as_view(), name='listar'),
    url(r'^registrar/$', UsuarioCrearAPIView.as_view(), name='registrar'),
    url(r'(?P<id>\d+)/editar/$', UsuarioEditarAPIView.as_view(), name = 'editar'),
    url(r'(?P<id>\d+)/eliminar/$', UsuarioEliminarAPIView.as_view(), name = 'eliminar'),
    url(r'auth-token/$', obtain_auth_token, name='token'),
    url(r'(?P<id>\d+)/$', UsuarioDetalleByIdAPIView.as_view(), name = 'detalle-id'),
    # url(r'(?P<email>.*)/$', UsuarioDetalleByEmailAPIView.as_view(), name = 'detalle-mail'),
   
]

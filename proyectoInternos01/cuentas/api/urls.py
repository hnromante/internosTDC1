from django.conf.urls import url
from django.urls import path, include

from .views import (
    UsuarioCrearAPIView,
    UserAPIViewset,
    UsuarioListarAPIView,
    UsuarioDetalleAPIView,
    UsuarioEditarAPIView,
    UsuarioEliminarAPIView
)
urlpatterns = [
    #url('',include(router.urls)),
    url(r'^$', UsuarioListarAPIView.as_view(), name='listar'),
    url(r'^registrar/$', UsuarioCrearAPIView.as_view(), name='registrar'),
    url(r'(?P<id>\d+)/$', UsuarioDetalleAPIView.as_view(), name = 'detalle'),
    url(r'(?P<id>\d+)/editar/$', UsuarioEditarAPIView.as_view(), name = 'editar'),
    url(r'(?P<id>\d+)/eliminar/$', UsuarioEliminarAPIView.as_view(), name = 'eliminar'),
]

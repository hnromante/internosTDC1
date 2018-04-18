from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('',views.ModuloViewset) VIEWSET GENERICA PARA TODOS LOS CASOS


urlpatterns = [
    url(r'^$',views.ModuloListView.as_view(),name='lista'),
    url(r'crear/$',views.ModuloCreateView.as_view(),name='crear'),
    url(r'(?P<id>\d+)/',views.ModuloDetalleView.as_view(), name='detalle'),
]
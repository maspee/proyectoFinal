from django.urls import path
from .import views


urlpatterns = [
    path('', views.publicacion, name='publicacion'),
    path('<int:pk>/', views.publicacion_detalle, name='publicacion_detalle'),
    path('publicacion/new', views.publicacion_nueva, name='publicacion_nueva'),
    path('<int:pk>/edit/', views.publicacion_editar, name='publicacion_editar'),
    path('<int:pk>/delete/', views.publicacion_eliminar, name='publicacion_eliminar'),
]
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('recetas', views.recetas, name='recetas'), 
    path('crud/crear', views.crear, name='crear'),
    path('crud/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('crud/editar/<int:id>', views.editar, name='editar'),
    path('envio', views.envio_mail, name='email'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
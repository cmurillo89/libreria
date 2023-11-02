from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('obtener_registros/', views.obtener_registros, name='obtener_registros'),
    path('crear/', views.crear, name='crear'),
    path('editar/', views.editar, name='editar'),
    path('form/', views.form, name='form'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'), # Tercera parte del curso de Django
    path('libros/editar/<int:id>/', views.editar, name='editar'), # cuarta parte del curso de Django
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # esta linea me ayuda ver las imagenes en el navegador
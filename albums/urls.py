from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('albums', views.albums, name='albums'),
    path('albums/crear', views.crear, name='crear'),
    path('albums/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('albums/editar/<int:id>', views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

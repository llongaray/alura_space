from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from galeria.admin import meu_admin_site  # Importe o MeuAdminSite aqui

urlpatterns = [
    path('admin/', meu_admin_site.urls),  # Use o urls do MeuAdminSite
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

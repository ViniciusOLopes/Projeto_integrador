from django.contrib import admin
from django.urls import path, include  # Certifique-se de incluir 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_gestao.urls')),  # Certifique-se de que o app_gestao.urls está correto
]

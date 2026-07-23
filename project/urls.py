from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Portal de Administração"
admin.site.site_title = "Sistema"
admin.site.index_title = "Painel de Controle"

urlpatterns = [
    path('', include('app.urls', namespace='app')),
    path(F'{settings.ADMIN_PANEL_PATH}/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

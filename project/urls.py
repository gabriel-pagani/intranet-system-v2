from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Template"
admin.site.site_title = "Sistema"
admin.site.index_title = "Painel de Controle"

urlpatterns = [
    # path('', include('app.urls', namespace='app')),
    path('admin/', admin.site.urls),
]

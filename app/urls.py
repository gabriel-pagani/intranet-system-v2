from django.urls import path
from app.views import ramais_view, ramais_json

app_name = 'app'

urlpatterns = [
    path('ramais/', ramais_view, name='ramais'),
    path('ramais/api/', ramais_json, name='ramais_json'),
]

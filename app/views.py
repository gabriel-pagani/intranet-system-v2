from app.models import Ramais
from django.http import JsonResponse
from django.shortcuts import render


def ramais_view(request):
    return render(request, 'app/ramais.html', {
        'is_staff': request.user.is_staff
    })


def ramais_json(request):
    dados = [
        {
            'name': ramal.get_display_name(),
            'phone': ramal.phone or '',
            'sector': ramal.sector.name if ramal.sector else '',
            'machine': ramal.machine or '',
        }
        for ramal in Ramais.objects.select_related('sector', 'user').all()
    ]
    return JsonResponse(dados, safe=False)

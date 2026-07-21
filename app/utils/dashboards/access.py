from django.db.models import Q
from app.models import Dashboards


def get_user_dashboards(user):
    if user.has_perm('app.view_all_dashboards'):
        return Dashboards.objects.all()

    return Dashboards.objects.filter(
        Q(usuarios_atribuidos=user) | Q(grupos_atribuidos__group__in=user.groups.all())
    ).distinct()
from django.core.exceptions import ValidationError


def valid_url(url):
    if url and not url.startswith('https://app.powerbi.com/'):
        raise ValidationError('Insira um link válido do Power BI.')

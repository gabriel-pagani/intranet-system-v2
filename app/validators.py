from django.core.exceptions import ValidationError


def valid_url(url):
    if url and not url.startswith('https://app.powerbi.com/'):
        raise ValidationError('Enter a valid Power BI url.')

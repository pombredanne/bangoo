from django.conf import settings
from django.utils.safestring import mark_safe

def act_theme(request):
    return {'ACT_THEME': getattr(request, 'ACT_THEME', settings.THEME)}
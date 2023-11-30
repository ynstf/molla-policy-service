from .PolicyPage import html_code
from django.http import JsonResponse

# Create your views here.

def policy(request):
    response = {
        'page': html_code
    }
    return JsonResponse(response)

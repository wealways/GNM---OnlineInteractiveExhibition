from django.shortcuts import render

# JSON response
from django.http import HttpResponse, JsonResponse

# csrf 허용
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def style_transfer(request):
    print('here')
    print(request.headers)

    return JsonResponse({'status': 'success'})
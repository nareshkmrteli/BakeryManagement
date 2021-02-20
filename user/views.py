from django.contrib.auth import get_user_model
from django.contrib.auth import login as userLogin
from django.contrib.auth import logout as userLogout
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['POST'])
def create(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    
    if username!='' and password !='':
        userModel = get_user_model()
        try:
            user = userModel(username=username)
            user.set_password(password)
            user.save()
            return JsonResponse({'detail':'User is register'})
        except(IntegrityError):
            return JsonResponse({'detail':'User is register'},status=409)
    else:
        return JsonResponse({'detail':'username and password field required'},status=400)
@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    
    if username!='' and password !='':
        userModel = get_user_model()
        try:
            user = userModel.objects.get(username=username)
            if user.check_password(password):
                userLogin(request,user)
                return JsonResponse({'detail':'user logined'})
            else:
                return JsonResponse({'detail':'invalid password or username'},status=401)
        except(ObjectDoesNotExist):
            return JsonResponse({'detail':'invalid password or username'},status=401)
    else:
        return JsonResponse({'detail':'username and password field required'},status=400)

@csrf_exempt
@require_http_methods(['POST'])
def logout(request):
    userLogout(request)
    return JsonResponse({'detail':'user is logout'})


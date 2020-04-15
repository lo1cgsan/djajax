# from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.http import JsonResponse


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    form_class = UserCreationForm


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Użytkownik o podanej nazwie już istnieje.'
    return JsonResponse(data)

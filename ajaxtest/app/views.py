from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
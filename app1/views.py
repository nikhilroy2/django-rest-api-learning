from django.shortcuts import render
from .models import PersonalInfo
# Create your views here.

def Homepage(request):
    personal_info = PersonalInfo.objects.all()
    context = {
        "personal_info": personal_info
    }
    print(personal_info)
    return render(request, 'app1/index.html', context=context)
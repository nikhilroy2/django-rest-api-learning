from django.shortcuts import render
from .models import PersonalInfo
from .helper import get_json_data
# Create your views here.

def Homepage(request):
    personal_info = PersonalInfo.objects.all()
    country_list = get_json_data('https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/index.json')
    context = {
        "personal_info": personal_info,
        "country_list": country_list
    }
    #print(country_list)
    #print(personal_info)
    return render(request, 'app1/index.html', context=context)
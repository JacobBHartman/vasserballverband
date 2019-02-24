from django.http import HttpResponse, JsonResponse
import requests
import json


# Create your views here.
def index(request):
    finish_list = requests.get("http://wasserballver.band/api/finishes").json()
    #return JsonResponse(finish_list, safe=False)
    
    top_ie = {}
    astring = str(type(finish_list))
    for finish in finish_list:
        if finish['tournament'] == 'http://wasserballver.band/api/tournaments/2018-19-inland-empire-pre-season/':
            team = requests.get(finish['team']).json()
            top_ie[team['name']] = finish['place']

    new_str = "Top 10 Inland Empire based on Pre-Season Power Rankings\n"
    for key, value in top_ie.items():
        new_str += str(value) + '.  ' + str(key) + '\n'
    new_str += "\ngithub.com/JacobBHartman/vasserballverband for the code base.\n\n"
    new_str += "add '/api' to view API backing this example app.\n\n"
    new_str += "Database is found at https://drive.google.com/open?id=1WACBT8g7Xl6jZ8iGL5IGLjWgAL_cv6genR43BOhwJzs\n\n"
    new_str += "The purpose of this page is to demonstrate an example app for the wasserballverband API.\n"
    new_str += "Imagine a publically editable database for all water polo-related data a la Wikipedia. The database feeds into an API. The API can be used to create powerful apps"
    return HttpResponse(new_str, content_type="text/plain")
   

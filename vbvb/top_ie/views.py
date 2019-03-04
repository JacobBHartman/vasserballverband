from django.shortcuts import render

import requests
import json

# Create your views here.
def index(request):
    finish_list = requests.get("http://wasserballver.band/api/finishes").json()
    url = 'http://wasserballver.band/api/tournaments/2018-19-inland-empire-pre-season/'

    top_ie = []
    idx = 1
    for finish in finish_list:
        if finish['tournament'] == url and finish['place'] == idx:
            team = requests.get(finish['team']).json()
            top_ie.append("{}. {}".format(idx, team['name']))
            idx += 1
    context = {}
    context['content'] = top_ie
    return render(request, 'top_ie/index.html', context)

from django.http import HttpResponse
from django.template import loader
from requests import get





# Create your views here.
def index(request):
    url = 'http://127.0.0.1:8000/api/teams'
    response = get(url)
    data = response.json()
    print(data, type(data))
    top_teams = [team['name'] for team in data]
    print(top_teams)
    return HttpResponse("You're looking at the top teams {}\n{}".format( top_teams[0], top_teams[1]))

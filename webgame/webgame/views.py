from django.http import HttpResponse
from django.shortcuts import render
import json
from . import game
import time
def index(request):
    return render(request,"index.html",{})
def fetch(request):
    # request - informacje od klienta (nick, controls etc.)

    # ustaw zmienną dt dla czasu (w milisekundach)
    dt = round(time.time() * 1000)
    # informacja zwrotna dla przeglądarki (co i jak ma wyświetlać)
    res = {
        "game":{
            "fps":10,
            "time":dt
        },
        # wykonaj funkcję manage, która zwraca listę postaci
        "creatures": game.manage(request)
    }
    # wysyłanie wiadomości do klienta (przeglądarki)
    # możesz ją podejrzeć (output) pod linkiem
    # http://127.0.0.1:8000/fetch/?data={%22name%22:%22Tosiek%22,%22controls%22:[]}
    return HttpResponse(json.dumps(res))
from django.http import HttpResponse
from django.shortcuts import render
import json
from . import game

def index(request):
    return render(request,"index.html",{})
def fetch(request):
    # request - informacje od klienta (nick, controls etc.)
    # informacja zwrotna dla przeglądarki (co i jak ma wyświetlać)
    res = {
        "game":{"fps":10},
        # wykonaj funkcję manage, która zwraca listę postaci
        "creatures": game.manage(request)
    }
    # wysyłanie wiadomości do klienta (przeglądarki)
    # możesz ją podejrzeć (output) pod linkiem : http://127.0.0.1:8000/fetch/?data={%22name%22:%22TEST%22}
    return HttpResponse(json.dumps(res))
import time
# zdefiniuj klasę:
class Creatures:
    # konstruktor - domyślne właściwości przy tworzeniu obiektu
    def __init__(self, name, param_dict = {}):
        self.name = name
        self.id = 10
        self.position = [34,-10,0]
        self.direction = 1
        self.health = 100
        self.maxHealth = 150
        self.sprite = "male_citizen"
        self.type = "player"
        self.text = "siema z django2"
        self.walk = 0
        self.speed = 8
        # nadpisz właściwości, z podanego dict'a
        for key in param_dict.keys():
            # setarr(na co?, klucz, skąd)
            setattr(self, key, param_dict[key])        
    # odświeżanie postaci, za każdym zapytaniem od klienta (przeglądarki)
    def update(self,controls):
        # drukowanie wciśniętych przycisków
        # print(controls)
        dt = round(time.time() * 1000)
        if(dt > self.walk):
            # zrób to jeśli creature jest graczem:
            if self.type == "player":
                key_down = False
                # jeśli kliknięta strzałka w prawo, dodaj pozycję i zmień kierunek
                if(39 in controls):
                    self.position[0] += 1
                    self.direction = 2
                    key_down = True
                if(37 in controls):
                    self.position[0] -= 1
                    self.direction = 3
                    key_down = True
                if(40 in controls):
                    self.position[1] += 1
                    self.direction = 1
                    key_down = True
                if(38 in controls):
                    self.position[1] -= 1
                    self.direction = 0
                    key_down = True
                if key_down:
                    self.walk = (dt + 1000/self.speed)
            else:
                # jeśli nie jest graczem ...
                pass
# lista zawierająca instancje klasy Creatures
creatureList = []
# lista zwierająca dict'y stworzone z instancji Creatures (wysyłane do klienta)
creatureListJSON = []

# Stwórz dane wszystkich potworów w grze
monsterList = [
    {
        "id":1,
        "name": "Dragon",
        "health" : 100,
        "maxHealth" : 100,
        "sprite" : "dragon",
        "position" : [33,-10,0],
        "type" : "monster"
    },
    {
        "id":2,
        "name": "Wizard",
        "health" : 100,
        "maxHealth" : 100,
        "sprite" : "orangeWizard",
        "position" : [35,-10,0],
        "type" : "monster"
    }
]

import json
# funkcja wykonująca się za każdym zapytaniem klienta (przeglądarki)
def manage(request):
    # jeśli nie ma żadnych potworów - stwórz je 
    if(len(creatureList) < 1):
        # stwórz potwory z listy monsterList
        for monster_params in monsterList:
            # stwórz potwora z klasy  Creatures 
            # WAŻNE! - podaj mu dict w 2 argumencie
            monster = Creatures(monster_params["name"],monster_params)
            # dodaj go do listy postaci (instancji obiektów)
            creatureList.append(monster)
            # dodaj go do listy dict'ów - do informacji wysyłanych do klienta
            creatureListJSON.append(monster.__dict__)
        
    # dane od klienta (nazwa, kliknięte przyciski etc.)
    data = json.loads(request.GET.get('data',''))
    # sprawdź, czy player jest na liście
    isPlayer = False
    for creature in creatureList:
        if data["name"] == creature.name:
            # jeśli jest, wykonaj metodę update 
            # (odśwież playera za każdym zapytaniem z przeglądarki)
            creature.update(data["controls"])
            isPlayer = True
    # jeżeli nie ma takiego playera - dodaj go: 
    if(not isPlayer):
        # stwórz playera z klasy  Creatures
        player = Creatures(data["name"])
        # dodaj go do listy postaci (instancji obiektów)
        creatureList.append(player)
        # dodaj go do listy dict'ów - do informacji wysyłanych do klienta
        creatureListJSON.append(player.__dict__)
    # zwróć listę wysyłaną do klienta
    return creatureListJSON
'''To jest przykładowy plik'''

# Drukuje tekst w konsoli
# print("Hello")

# pojedyńczy gracz (dict)
player = {
  "nick" : "Ziom",
  "level" : 120,
  "speed" : 2,
  "hp" : 120
}
# rozwiązanie ćw1:
# print("Gracz "+player["nick"]+" ma poziom "+str(player["level"]))

# Tablica pojedyńczych graczy (dicts)
arr = [
  {
    "nick" : "Ziom",
    "level" : 100,
    "speed" : 2,
    "hp" : 120
  },
  {
    "nick" : "Ziom2",
    "level" : 10,
    "speed" : 1,
    "hp" : 0
  }
]
# Rozwiązanie ćw 2
# print(arr[0]["nick"]+" ma "+str(arr[0]["level"]))
# print(" poziom, a "+arr[1]["nick"]+" ma "+str(arr[1]["level"]))

# kolejny pojedyńczy gracz
player3 = {
  "nick" : "Ziom3",
  "level" : 70,
  "speed" : 1,
  "hp" : 30
}

# kolejka
from collections import deque
quene = deque(arr)
quene.append(player3)
# print(quene)
# quene.popleft();
# print(quene)

# Rozwiązanie ćwiczenia z IF
# if quene[0]["level"] > 50:
#   print(quene[0]["nick"])
# if quene[1]["level"] > 50:
#   print(quene[1]["nick"])

# Rozwiązanie ćwiczenia z FOR
# for q in quene:
#   if 50 < q["level"]:
    # print(q)

# PRZYKŁADY BREAK I CONTINUE
# c = [1,2,3,4,5,6,7,8,9]
# for a in c:
#   if a == 4:continue
#   print(a)
# for q in quene:
#   if q["level"] > 50 or q["hp"] > 100:
#     print(q)

# FUNKCJE [prostszy przykład]
# def dodaj(a = 2,b = 4):
#   # print(a+b)
#   return a+b

# x = dodaj(5,10)
# y = dodaj(b = x)
# print(y)

# Rozwiązanie ćwiczenia z funkcji.
# def addExp(player,exp = 20):
#   player["level"] += exp
#   player["hp"] += exp/2
# print(arr)
# for p in arr:
#   addExp(p)
# print(p)
arr = [
  {
    "nick" : "Ziom",
    "level" : 100,
    "speed" : 2,
    "hp" : 120
  },
  {
    "nick" : "Ziom2",
    "level" : 10,
    "speed" : 1,
    "hp" : 0
  }
]

names = ["Jarek","Grzesiek","Marysia","Piotrek","Zenon"]

# RANGE
# for i in range(3):
  # print(names[i])

#LEN
# print(len(names))

#DOCSTRINGS
def func():
  '''Ta funkcja nic nie robi'''
  return None;

print(__doc__)
# print(print.__doc__)
# print(func.__doc__)
# help(print)
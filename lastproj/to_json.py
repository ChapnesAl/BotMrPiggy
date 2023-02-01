import json


ar = []

with open('cenz.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0] # перевод в нижний регистр, в [] указываем что пропускаем пустые строки
        if n != '': # пропускаем  строки пустые с пробелами
            ar.append(n)
with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar,e)
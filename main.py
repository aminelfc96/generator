import json
from datetime import datetime, timedelta
import random

with open('db.json', 'r') as file:
    db: dict = dict(json.load(file))
    
state: dict = db["state"]
level: dict = db["level"]

print("Niveau disponible", end=": ")
for l in level:
    print(l, end=", ") 
print()
    
choosed_level = input("Choisi le niveau: ")
starting_day = input("Date de debut d'examen aaaa-mm-jj: ")

def gen(lvl):
    short = level[lvl]
    i = 0
    for module in short:
        date_time_obj = datetime.strptime(starting_day, '%Y-%m-%d')
        date = date_time_obj + timedelta(days=i)
        while True:
            prof_garde = random.choice(list(short.values()))
            if state[prof_garde] == 1 and prof_garde != short[module]:
                print(f'Date {date} | Module {module} | Prof Responsable {short[module]} | Prof Garde {prof_garde} ')
                break
        i+=1
                
        
gen(choosed_level) 

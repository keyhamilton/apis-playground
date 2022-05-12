import json, sys
from datetime import datetime

year = str(datetime.today().year)


try:
    if sys.argv[1]:
        year = sys.argv[1]
except:
    pass

total = 0

with open('calendar.json') as calender:
        try:
            data = json.load(calender)

            filtro = ['Observance', 'Data comemorativa']

            

            holydays = data["items"]

            for k in holydays:
                if filtro[0] not in k['description'] and filtro[1] not in k['description'] and k['start']['date'][:4] == year:
                    total += 1
                    print('-'*100)
                    print(' '*(50-len(k['summary'])//2),k['summary'])
                    print(' '*(50-len(k['description'])//2), k['description'])
                    print(' '*(50-len(k['start']['date'])//2), k['start']['date'])
                    print('-'*100)

            
            
        except:
            print("Oops! Sinto muito, nada foi encontrado. Tente novamente com uma nova entrada.")

if total == 0:
    print('Ainda não existe um calendário para o ano especificado. Tente novamente com {} ou {}'.format(datetime.today().year+1, datetime.today().year-1))
else:
    print('{} feriados'.format(total))
    print('-'*11)

calender.close()




    
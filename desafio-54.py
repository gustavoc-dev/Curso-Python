from datetime import datetime
count = 0
count2 = 0

for c in range(0,4):
    birth = input('Digite uma data de aniversário:\n')
    data = datetime.strptime(birth, "%d/%m/%Y")

    calc = datetime.now().year - data.year
    if  calc >=21:
        count+=1
    elif calc <=21:
        count2+=1

print('Foram inseridos {} maiores de idade e {} menores de idade'.format(count,count2))

# Objetivo geral, trabalhar com datas, horas e fusos horários em python utilizando datetime

from datetime import datetime, date, timedelta

d = date(2024, 9, 8)
print(d)
print()
print(datetime.now())
print()
print(datetime.today())

d = d + timedelta(weeks=1)
print(d) # adicionou uma semana a data de cima, funciona com days / minutes alem de weeks

# usando strftime e strptime
d2 = datetime.now()

# formatando data e hora
print(d2.strftime("%d/%m/%Y %H:%M"))

# convertendo string para datetime
date_string = '20/07/2023 15:30'
d3 = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d3)
# também é possivel pegar uma data ou um datetime.now e converter 
# ele para algum formato que vocÇe desejar

# utilizando o pytz para trabalhar com fuso horario

import pytz

# criando datetime com timezone

br_time = datetime.now(pytz.timezone("America/Sao_Paulo")) 
# os codigos de timezone estão presentes na documentação da lib
eu_time = datetime.now(pytz.timezone("Europe/Oslo")) 

print(br_time)
print()
print(eu_time)

# da pra fazer sem o pytz, mas é muito mais verboso e desnecessário.
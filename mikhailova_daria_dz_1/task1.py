duration = int(input('Введите секунды:'))
day = duration//(60*60*24)
hours = (duration % (60*60*24))//(60*60)
minut = ((duration % (60*60*24)) % (60*60))//60
sek = ((duration % (60*60*24)) % (60*60)) % 60
if day < 1 and hours < 1 and minut < 1:
    print(sek,'сек')
elif day < 1 and hours < 1:
    print(minut,'мин',sek,'сек')
elif day < 1:
    print(hours,'час',minut,'мин',sek,'сек')
else:
    print(day,'дн',hours,'час',minut,'мин',sek,'сек')

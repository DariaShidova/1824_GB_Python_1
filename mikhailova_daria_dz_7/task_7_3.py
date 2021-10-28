import os
import shutil
#Я ТОЛЬКО СЕЙЧАС ПОНЯЛА ЧТО СДЕЛАЛА СОВСЕМ НЕ ТООООО
#сама придумала себе задание, подумала что надо просто папки которые внутри переложить в новую
#НАДЕЮСЬ УСПЕЮ ИСПРАВИТЬ ДО ТОГО КАК ВЫ ПРОВЕРИТЕ :((((
folder = 'templates'
main_folder = 'my_project'
creation = (os.path.join(main_folder, folder))

for root, dirs, files in os.walk(main_folder):
    if not os.path.isdir(creation):
        os.makedirs(creation)
    try:
        for d in dirs:
            if d != folder:
                new_location = shutil.move(f'{main_folder}/{d}', f'{creation}/{d}')
    except FileNotFoundError as e:
        print(f'error: {e}')

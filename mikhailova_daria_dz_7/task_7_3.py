import os
import shutil

folder = 'templates'
main_folder = 'my_project'
creation = (os.path.join(main_folder, folder))

for root, dirs, files in os.walk(main_folder):
    print(dirs,files)
    if not os.path.isdir(creation):
        os.makedirs(creation)
    #try:
    #    for d in dirs:
    #        if d != folder:
    #            new_location = shutil.move(f'{main_folder}/{d}', f'{creation}/{d}')
    #except FileNotFoundError as e:
    #    print(f'concrete error: {e}')

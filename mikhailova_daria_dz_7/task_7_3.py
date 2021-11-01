import os
import shutil
#не уверенна что нужно было сделать именно это.

folder = 'templates'
main_folder = 'my_project'
format_file = '.html'

creation = (os.path.join(main_folder, folder))
if not os.path.isdir(creation):
    os.makedirs(creation)

for root, dirs, files in os.walk((os.path.normpath(main_folder)), topdown=False):
    try:
        for file in files:
            if file.endswith(format_file):
                print(root)
                folder_in_file = root.split('\\')[-1]
                new_location = os.path.join(creation, folder_in_file)
                shutil.copytree(root, new_location)
    except FileExistsError as e:
        break

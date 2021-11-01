import os
import shutil

name_folder = ['settings', 'mainapp', 'adminapp', 'authapp']
main_folder = 'my_project'
storage = os.getcwd()

for i in name_folder:
    creation = (os.path.join(storage, main_folder, i))
    if not os.path.isdir(creation):
        os.makedirs(creation)

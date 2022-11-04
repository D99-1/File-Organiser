import os 
import shutil
# IMPORTANT: Use `pip install tqdm`
from tqdm import tqdm

from_dir = input("Enter Original Directory Path: ")
to_dir = input("Enter New Directory Path: ")


[os.rename(os.path.join(from_dir, f), os.path.join(from_dir, f).replace(' ', '_').lower()) for f in os.listdir(from_dir)]
list_of_files = os.listdir(from_dir)
list_of_dir = []
list_of_files_only = []
startsWithDot = 0
continueWithDot = ""

for y in list_of_files:
    if(y.startswith('.') and y != '.DS_Store'):
        startsWithDot =+1
print(startsWithDot)
if(startsWithDot > 0):
    continueWithDot = input("\nYour Folder Contains A Folder Or File Starting With '.'\nThis Can Distrupt The Functioning Of This Program\nOnly Continue If You Have Run This Program Before And The Folder/File Was Created By It\nWould You Like To Continue? [y/n] ")
    print("")

if(continueWithDot == 'y' or startsWithDot == 0):
    for x in list_of_files:
        if (os.path.isdir(from_dir+'/'+x) and x != '.DS_Store' and x.startswith('.') == False):
            list_of_dir.append(x)
            print(list_of_dir)

    for x in list_of_files:
        if (os.path.isfile(from_dir+'/'+x) and x != '.DS_Store'):
            list_of_files_only.append(x)

    if(len(list_of_files_only) != 0):
        with tqdm(total=len(list_of_files)) as pbar:
            for file_name in list_of_files:
                name, extension = os.path.splitext(file_name) 
                if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
                    path1 = from_dir + '/' + file_name
                    path2 = to_dir + '/' + ".Images"
                    path3 = to_dir + '/' + ".Images" + '/' + extension
                    path4 = to_dir + '/' + ".Images" + '/' + extension + '/' + file_name
                    if os.path.exists(path2):
                        if os.path.exists(path3):
                            #print("Moving "+file_name)
                            shutil.move(path1, path4)
                        else:
                            os.makedirs(path3)
                            #print("Moving "+file_name)
                            shutil.move(path1,path4)
                    else:
                        os.makedirs(path2)
                        os.makedirs(path3)
                        #print("Moving "+ file_name)
                        shutil.move(path1, path4)
                elif extension:
                    path1 = from_dir + '/' + file_name
                    path2 = to_dir + '/' + extension
                    path3 = to_dir + '/' + extension + '/' + file_name
                    if os.path.exists(path2):
                        #print("Moving "+file_name)
                        shutil.move(path1, path3)
                    else:
                        os.makedirs(path2)
                        #print("Moving "+ file_name)
                        shutil.move(path1, path3)
                pbar.set_description('Moving Files')
                pbar.update(1)

    if(list_of_dir != []):
        with tqdm(total=len(list_of_dir)) as pbar:
            for dirs in list_of_dir:
                files = os.listdir(from_dir + '/'+dirs)
                path1 = from_dir + '/' + dirs
                path2 = to_dir + '/' + ".Folders"
                path3 = to_dir + '/' + ".Folders" + '/' + dirs
                if(os.path.exists(path2)):
                    if(os.path.exists(path3)):
                        pass
                    else:
                        os.makedirs(path3)
                else:
                    os.makedirs(path2)
                    os.makedirs(path3)
                for file_names in files:
                    route1 = from_dir + '/' + dirs + '/' + file_names
                    route2 = to_dir + '/' + '.Folders' + '/' + dirs + '/' + file_names
                    shutil.move(route1,route2)
                os.removedirs(from_dir+'/'+dirs)
                pbar.set_description('Moving Folders')
                pbar.update(1)
    print("Success!")
else:
    print("\nProgram exited due to user intervention")
                
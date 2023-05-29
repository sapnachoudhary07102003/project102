import os
import shutil

source="C:/Users/Ramgopal/Downloads/C102_assets-main"
destination="C:/Users/Ramgopal/Desktop/shift"


content = os.listdir(source)
#print(content)

for val in content:
    name, ext = os.path.splitext(val)

    if ext == '':
        print("continue")

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = source +'/'+"file-name"
        path2 = destination + '/' + "shift"  
        path3 = destination + '/' + "shift" + '/' + "file-name" 

        if os.path.exists(path2):
          print("Moving " + val + ".....")
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + val + ".....")
          shutil.move(path1, path3)
       


    
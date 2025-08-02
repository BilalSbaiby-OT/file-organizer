import os
import shutil
import csv

def save_Data(data):
    with open("data.csv", "w" , newline = "") as f:
        writer= csv.writer(f)
        writer.writerows(data)

folder_path = input("enter folder path: ")
save_Data(f"folder path {folder_path}")
if os.path.exists(folder_path):

    files = os.listdir(folder_path)
    for f in files:
        full_path = os.path.join(folder_path, f)
        if os.path.isfile(full_path):
            name,extension = os.path.splitext(f)
            save_Data([f"Processing file: {f} with extension {extension}"])
            print(f"{f} hvae extension {extension}")
            folder_name = extension[1:] if extension else "no_extension"
            new_folder_path = os.path.join(folder_path, folder_name)
            save_Data(f"create the direct path to the file {new_folder_path}")
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                print(f"created folder: {new_folder_path}")
            shutil.move(full_path,os.path.join(new_folder_path, f))
            save_Data(f"moved files to the folder {new_folder_path}")

        else:
            print("not a file")
            save_Data([f"{f} is not a file."])
else:
    print("folder does not exists")
    save_Data(["Folder does not exist."])
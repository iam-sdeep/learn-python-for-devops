import shutil
import os
import datetime

def create_backup(source_path,destination_path):

    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path,f"backup_{date_name}")
    try:
        shutil.make_archive(backup_name,'gztar',source_path)
        print("Backup Completed")
    except Exception as e:
        print(e)

source_path = input("Enter source path: ") #"/home/subhradeep/python-for-devops"
destination_path = input("Enter destination path: ") #"/home/subhradeep/backups"

create_backup(source_path,destination_path)
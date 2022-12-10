# import sqlite3
# import dbInitializer as db
#import psutil
# import os
# import platform
import logging as log
# import logger
import dbOperations as db
import glob
import os
import sendEmail as sendEmail

# from prettytable import PrettyTable

# import csv
# from datetime import datetime
import time

print('Inizio')
# connessione sqlite
con = db.sqliteConn()
print('Connessione effettuata')
# inizializzazione db
# db.sqliteInitialize(con)


dir_name = 'C:/Users/diego.ITIFS/Downloads'

print('Dir_name:' + dir_name)

# Get a list of files (file paths) in the given directory
list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/**/*', recursive=True))

# get list of ffiles with size
files_with_size = [(file_path, os.stat(file_path).st_size)
                   for file_path in list_of_files]

# Iterate over list of tuples i.e. file_paths with size
# and print them one by one
for file_path, file_size in files_with_size:
    # print('file_path:' + file_path)
    db.insertRow(con, file_path)

i = db.checkIfRunning(con)
print(i)
if i == 0:
    print(i)
    sendEmail.send_email()
    i = 0

db.store_current(con)

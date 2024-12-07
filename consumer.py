import datetime
import random
import json
import shutil
import os
import time

class TestClass:
    def __init__(self , title, body):
      dt = datetime.datetime.now()
      self.tile = title   
      self.body = body
      self.date_time = dt.strftime("%Y-%m-%d %H:%M:%S")
      self.likes = random.randint(10, 100)

_PATH_DOWNLOAD = "Download/"
_PATH_ERROR = "Error/"
_PATH_LOADED = "Loaded/"

def get_files():
   f = []
   for (dirpath, dirnames, filenames) in os.walk(_PATH_DOWNLOAD):
      f.extend(filenames)
      break
   print(f)
   return f

def read_files(path):
   with open(path, "r") as f:
         load_json = json.load(f)
         return load_json

def json_to_ts(js):
    try:
        if(js['className'] == 'TestClass'):
            #raise Exception('TEST my exception')
            ts = TestClass(title=js['title'], body=js['body'])
            ts.likes = js['title']
            ts.date_time = js['date_time']
            return ts
    except Exception as er:
        print(er)

def wath_dir():
    files = get_files()
    for file in files:
        path = f"{_PATH_DOWNLOAD}{file}"
        json_content = read_files(path)
        ts = json_to_ts(json_content)
        if(ts == None):
            print('------------ERROR------------')
            shutil.copyfile(path, f"{_PATH_ERROR}{file}")
        else:
            print(f'------------Появилась переменная: {ts}------------')
            shutil.copy(path, _PATH_LOADED)
        os.remove(path)

while True:
    time.sleep(1)
    wath_dir()

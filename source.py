from datetime import datetime
import json
import random
import sched
import time

DOWNLOAD_DIR = "Download/"
TOTAL_COUNT = 5
_TIME_SEC = 0.25
_J = 0

class TestClass:
    def __init__(self , title, body):
      dt = datetime.now()
      self.title = title
      self.body = body
      self.date_time = dt.strftime("%Y-%m-%d %H:%M:%S")
      
def to_dic(o):
   result = o.__dict__
   result["className"] = o.__class__.__name__
   return result

def send_json_data(i):
   try:
      title = f'Header - {random.randint(1, 9999)}'
      body = f'Some content - {random.randint(1000, 9999999)}'
      ts = TestClass(title, body)
      fd = f'Download/{i}-{datetime.now().strftime("%Y%m%d%H%S")}-data.json'
      with open(fd, "x") as f:
         json.dump(ts, f, default = to_dic)
      print(f'Отправка {i} выполнена')
   except Exception as err:
      print(f'ошибка отправки {i} - {err}')

def do_work(scheduler):
   global _J
   _J = _J + 1
   print(f'----{_J}----')
   send_json_data(_J)
   if _J < TOTAL_COUNT:
      s.enter(_TIME_SEC, 1, do_work, (scheduler,))

print('__START__')

s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, do_work, (s,))
s.run()

print('__STOP__')

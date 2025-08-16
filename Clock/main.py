import datetime
from playsound import playsound
alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
alarm_min = int(input("Enter the minute for the alarm (0-59): "))
alarm_am = input("Am/Pm: ")
if alarm_am.lower() =="pm":
 alarm_hour +=12
while True:
 if alarm_hour==datetime.datetime.now().hour and alarm_min==datetime.datetime.now().minute:
  print("Wake up!")
  playsound('punky.mp3')
  break
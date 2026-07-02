from subprocess import Popen
from time import sleep
from sys import argv

def notify():
    Popen("mpv notif.mp3 >> /dev/null", shell=True)

i = 0
pomo_count = 0
work_minutes = 25
rest_minutes = 5
long_rest_minutes = 30

work_message = f"notify-send \"Paradox Pomodoro\" \"It's time to work for {work_minutes} minutes\""
rest_message = f"notify-send \"Paradox Pomodoro\" \"It's time to rest for {rest_minutes} minutes"
long_rest_message = f"notify-send \"Paradox Pomodoro\" \"It's time to rest for {long_rest_minutes} minutes"

while(True):
    while True:
        notify()
        Popen(work_message, shell=True)
        sleep(work_minutes)
        pomo_count+=1
        if pomo_count % 4 != 0:
            notify()
            Popen(rest_message + f"\nPomodoro Count = {pomo_count}\"", shell=True)
            sleep(rest_minutes)
            i+=1
        else:
            notify()
            Popen(long_rest_message + f"\nPomodoro Count = {pomo_count}\"", shell=True)
            sleep(long_rest_minutes*60)
            i=0

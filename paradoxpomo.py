#!/bin/python3

from subprocess import Popen
from time import sleep
from sys import argv
from os import path


pomo_count = 0
work_minutes = 25
rest_minutes = 5
long_rest_minutes = 30
pomo_count_per_cycle = 4
notif_sound = "notif.mp3"

script_dir = path.dirname(path.realpath(__file__))

def notify():
    Popen(f"mpv {script_dir}/{notif_sound} >> /dev/null", shell=True)

if "0" in argv:
    print("Error: Cannot set any value to zero.")
    exit()
elif len(argv) >= 2 and len(argv) == 5:
    work_minutes = int(argv[1])
    rest_minutes = int(argv[2])
    long_rest_minuts = int(argv[3])
    pomo_count_per_cycle = int(argv[4])
elif len(argv) >= 2 and len(argv) != 5:
    print("Usage: paradoxpomo.py <work minutes> <rest minutes> <long rest minutes> <pomodoro count before long rest>")
    exit()
    
work_message = f"notify-send \"Paradox Pomodoro\" \"It's time to work for {work_minutes} minutes\""
rest_message = f"notify-send \"Paradox Pomodoro\" \"It's time to rest for {rest_minutes} minutes"
long_rest_message = f"notify-send \"Paradox Pomodoro\" \"It's time to rest for {long_rest_minutes} minutes"

while(True):
    while True:
        notify()
        Popen(work_message, shell=True)
        sleep(work_minutes*60)
        pomo_count+=1
        if pomo_count % pomo_count_per_cycle != 0:
            notify()
            Popen(rest_message + f"\nPomodoro Count = {pomo_count}\"", shell=True)
            sleep(rest_minutes*60)
        else:
            notify()
            Popen(long_rest_message + f"\nPomodoro Count = {pomo_count}\"", shell=True)
            sleep(long_rest_minutes*60)

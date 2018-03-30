import psutil
from tkinter import *
from tkinter import messagebox

while(1):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"
    ##print(percent+'% | '+plugged)
    status = percent
    if(status == '80'):
        messagebox.showwarning(message=percent+'% | '+plugged)
        break

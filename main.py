import os
import subprocess
import threading
import time
charge = subprocess.check_output("upower -i $(upower -e | grep BAT) | grep --color=never -E percentage|xargs|cut -d' ' -f2|sed s/%//", shell = True)
charge.decode("utf-8")
charge=int(charge)
def alert():
    if charge <= 20:
        os.system("notify-send Battery_Status 'Charger Mangta Hai APUN ko '")
    elif charge >= 90:
        os.system("notify-send Battery_Status 'OverChargeAlert!'")
def statuscheck():
    x=subprocess.check_output("upower -i $(upower -e | grep BAT) | grep --color=never -E state|xargs -e", shell=True)
    x=str(x.decode("utf-8"))
    if "discharging" in x:
        return(1)
    else:
        return(0)
def main():
    while 1==1:
        state=statuscheck()
        if state == 1 and charge <= 20:
            alert()
        elif state == 0 and charge >= 90:
            print("overcharge")
            alert()
        time.sleep(120)
main()
        


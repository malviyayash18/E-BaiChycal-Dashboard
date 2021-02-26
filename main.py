import eel
import random

eel.init('web')

if __name__ == "__main__":
    print("Console is Working !!!")
    eel.start('Dashboard.html', mode='electron', block=False, size=(800, 480))


percent = 0
while True:
    eel.updateBatteryHandler(percent)
    eel.sleep(0.1)
    percent = percent + 1
    print(percent)

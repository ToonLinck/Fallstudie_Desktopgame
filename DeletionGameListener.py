import time
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
import subprocess

class DeletionHandler(FileSystemEventHandler):                              # creates the DeletionHandler class
    def on_deleted(self, event: FileSystemEvent):                           # creates the on_deleted method
        splitted_path = str(event.src_path).split("\\",)
        length = len(splitted_path)-1
        file_name = splitted_path[length]
        print(f"File '{file_name}' got deleted.")
        
        subprocess.call(["python","Game.py",file_name])                     # calls the Game.py and parses the name of the deleted file
        return

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # gets the path to the desctop with the environment variable USERPROFILE

observer = Observer()                                                       # creates a observer from the watchdog library
event_handler = DeletionHandler()                                           # creates a DelistionHandler

watch = observer.schedule(event_handler, desktop, recursive=True)           # schedules the watcher of desctop and calls the DeletionHandler

observer.start()                                                            # starts the observer                                                                

try:
    while (observer.is_alive):                                              # checks if the thread is still activ
        time.sleep(1)                                                       # Necessary because the programm cant be stopped clean without it
except KeyboardInterrupt:                                                   # checks if strg C has been pressed in the console
    observer.stop()                                                         # deactivates the thread
    observer.join()                                                         # blocks the thread
    print("stopped all processes of breakout listener")
finally:
    observer.stop()
    observer.join()
    print("Program stopped")

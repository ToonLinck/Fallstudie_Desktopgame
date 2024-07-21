import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
import logging


class DeletionHandler(FileSystemEventHandler):
     def on_deleted(self, event: FileSystemEvent):
          print(event.src_path)
          print("file deleted")
          #Gelöschte Datei erkannt, Breakout wird gestartet


if __name__ == "__main__":
    print("Breakout Listener Startup")

    # Der oberste Dateipfad, bei dem der Watchdog die observation beginnt
    ground_path = os.path.abspath(os.sep)
    
    # ein Eventhandler wird erstellt 
    event_handler = DeletionHandler()
    observer = Observer()
    observer.schedule(event_handler, ground_path, recursive=True )
    observer.start()

    try: 
         while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print("stopped all processes of breakout listener")




#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 




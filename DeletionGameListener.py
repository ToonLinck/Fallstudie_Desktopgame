import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

class DeletionHandler(FileSystemEventHandler):                              # kriert die Klasse DeletionHandler
    def on_deleted(self, event: FileSystemEvent):                           # kriert die on_deleted Methode der Klasse
        print(event.src_path)
        print("file deleted")

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # holt den Pfad zum Desktop mittles der Umgebungsvariable USERPROFILE

observer = Observer()                                                       # kreirt einen Observer von der watchdog Bibliothek
event_handler = DeletionHandler()                                           # kreiert einen DelistionHandler

watch = observer.schedule(event_handler, desktop, recursive=True)           # plant die Überwachung vom Desktop und ruft den DeletionHandler auf

observer.start()                                                            # startet den Observer                                                                

try:
    while (observer.is_alive):                                              # checkt ob der Thread noch aktiv ist
        time.sleep(1)                                                       # Ist nötig, da man das Programm sonst nicht beenden kann
except KeyboardInterrupt:                                                   # checkt ob strg C in der Konsole gedrückt wurde
    observer.stop()                                                         # deaktiviert den Thread
    observer.join()                                                         # blockt den Thread
    print("stopped all processes of breakout listener")
finally:
    observer.stop()
    observer.join()
    print("Stuff happend")
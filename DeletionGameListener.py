import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

_listenign = True


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

observer = Observer()
event_handler = LoggingEventHandler()

observer.schedule(event_handler, desktop, recursive=False )


observer.start()

while (observer.is_alive)
    try 

event_handler.on_deleted += function () => {

}
#!/usr/bin/env python

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Mod the class and the on create method
class ChangeHandler(FileSystemEventHandler):

    # Chmod on create a python file
    def on_created(self, event):
        if self.get_ext(event.src_path) == '.py':
            os.chmod(event.src_path, 488)

    #Get the file extension."
    def get_ext(self,filename):
        return os.path.splitext(filename)[-1].lower()

if __name__ == "__main__":
    # Setup watchdog
    sys_path = "/home/pi/"
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=sys_path, recursive=True)
    observer.start()

    # Try and loop
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/Kalpa Kularathne/Downloads'

#Event Handler Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")
    
    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")
    
    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")

#Initializing Even Handler
event_handler = FileEventHandler()

#Initializing Observer
observer = Observer()

#Sheduling the observer
observer.schedule(event_handler, from_dir, recursive=True)

#Starting the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
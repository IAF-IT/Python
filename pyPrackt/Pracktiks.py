from watchdog.observers import Observer
import os
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)


folder_track = '/Users/iafar/Desktop'
folder_dest = '/Users/iafar/Desktop/Photo'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
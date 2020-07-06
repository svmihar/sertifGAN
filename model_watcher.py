from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler as pmh
import sys
import os
import time


def on_created(event):
    print(f"{event.src_path} created.")
    print("uploading to drive")
    os.system(f"drive add_remote --file {event.src_path}")

    path_list = event.src_path.split('/')
    path = '/'.join(path_list[:-1])
    files = get_files(path)
    if len(files)>2: 
        delete_files(files[:-2])


def get_files(path): 
    return sorted([f'{path}/{a}' for a in os.listdir(path)])

def delete_files(files): 
    for f in files: 
        os.remove(f)
        print(f'{f} deleted')

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "./models/default/"
    handler = pmh("*.pt", "", False, True)
    handler.on_created = on_created
    my_observer = Observer()
    my_observer.schedule(handler, path, recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

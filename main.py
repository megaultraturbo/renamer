# TODO
# dodawanie nazwy folderu do nowej nazwy pliku
# Systemy operacyjne [25.03.2022]

from datetime import date
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import rename
from os import chdir


class Watcher:
    dir = "C:/Users/jakub/OneDrive - The Opole University of Technology/semestr 4/systemy operacyjne"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.dir, recursive=True)
        self.observer.start()
        try:
            print("loooool")
        except:
            self.observer.stop()
            print("HUJ")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == "created":
            # print("DODANO PLIKA %s." % event.src_path)
            filename = event.src_path
            dir = "C:/Users/jakub/OneDrive - The Opole University of Technology/semestr 4/systemy operacyjne"
            chdir(dir)
            renameX(filename)


def renameX(filename):
    today = str(date.today())
    formatted = "[" + today[8:10] + "." + today[5:7] + "." + today[0:4] + "].png"
    rename(filename, formatted)


if __name__ == '__main__':

    w = Watcher()
    w.run()

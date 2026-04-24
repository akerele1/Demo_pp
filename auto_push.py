import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AutoPush(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or ".git" in event.src_path:
            return
        print(f"Change detected: {event.src_path}")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Auto save: {event.src_path}"])
        subprocess.run(["git", "push"])

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(AutoPush(), path=".", recursive=True)
    observer.start()
    print("Watching for changes... Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

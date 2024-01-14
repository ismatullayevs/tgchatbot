import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.event_type not in ['modified', 'created', 'moved', 'deleted']:
            return
        if event.is_directory or not event.src_path.endswith('.py'):
            return

        logger.info(f'Restarting due to change in {event.src_path}')
        restart()


def run():
    return subprocess.Popen(['python3', 'main.py'])


def restart():
    global process
    try:
        process.terminate()
        process.wait()
    except Exception as e:
        logger.exception(f"Error while restarting: {e}")
    process = run()


if __name__ == '__main__':
    process = run()

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

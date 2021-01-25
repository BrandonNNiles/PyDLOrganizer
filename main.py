from functions import get_download_dir
from heleprs import *
import time


version = 0.1
interval_sec = 5

def main_loop():
    starttime = time.time()
    while True:
        print("Attempting to organize downloads")
        time.sleep(interval_sec - ((time.time() - starttime) % interval_sec))


if __name__ == '__main__':
    clear_window()
    print("Download Organizer v{} Initialized!".format(version))
    print("Downloads folder: {}".format(get_download_dir()))
    main_loop()


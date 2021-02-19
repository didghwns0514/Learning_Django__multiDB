from django.apps import AppConfig
from threading import Thread

import time
import datetime

class TestThread(Thread):
    """
    running thread here
    참조 >>>
    https://stackoverflow.com/questions/59541954/how-to-start-a-background-thread-when-django-server-is-up
    """
    def run(self):
        while True:
            print(f'Thread running... : {datetime.datetime.now()}')
            time.sleep(1)

class StoreappConfig(AppConfig):
    name = 'storeapp'

    # def ready(self):
    #     TestThread().start()

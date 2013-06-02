#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thinkathon.settings")

    from potholes import tasks
    from threading import Thread

    twitter_thread = Thread(target=tasks.twist_listener)
    twitter_thread.setDaemon(True)
    twitter_thread.start()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

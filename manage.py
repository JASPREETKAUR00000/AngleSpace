#!/usr/bin/env python
import os
import sys
import django

# Set settings module to the current app.py config
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app")  # 'app.py' is your settings file

django.setup()

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)

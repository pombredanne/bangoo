#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    ### Add bangoo to sys path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examplesite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
#<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "images.settings")
#=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battleNet.settings")
#>>>>>>> 545165cbca60ecbd840e7aa6b6d16cc4b2590188

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

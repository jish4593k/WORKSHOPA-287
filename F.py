#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import torch
import torchvision
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Perform a PyTorch-related task'

    def add_arguments(self, parser):
        parser.add_argument('--example_arg', type=str, help='An example argument for the command')

    def handle(self, *args, **options):
        # Your PyTorch-related code goes here
        example_arg = options['example_arg']
        print(f'Performing PyTorch-related task with example_arg: {example_arg}')

        # Your Django-related code goes here
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_project.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # You can still run other Django management commands here if needed
    Command().execute()

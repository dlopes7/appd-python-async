#!/usr/bin/env python
import os
import sys

from appdynamics.agent import api as appd

if __name__ == '__main__':

    appd.init(
        {'APPD_APP_NAME': 'Python',
         'APPD_TIER_NAME': 'django',
         'APPD_NODE_NAME': 'dlopes-mac',
         'APPD_CONTROLLER_HOST': 'controller',
         'APPD_CONTROLLER_PORT': '8090',
         'APPD_ACCOUNT_ACCESS_KEY': 'access_key',
         'APPD_LOGGING_LEVEL': 'debug'
         }
    )

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appdasync.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

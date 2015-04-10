#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',

            'bangoo', 'bangoo.navigation', 'bangoo.content',
            'tests',
        ],
        MIDDLEWARE_CLASSES = ()
    )

django.setup()

from django.test.simple import DjangoTestSuiteRunner

def run_tests():
    test_runner = DjangoTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)

if __name__ == '__main__':
    run_tests()
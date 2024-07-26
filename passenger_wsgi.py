# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/d/dmakger/api.fotoprintart.ru')
sys.path.insert(1, '/home/d/dmakger/api.fotoprintart.ru/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

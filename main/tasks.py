#!-*-coding:utf-8-*-
import logging
from celery.exceptions import SoftTimeLimitExceeded

from just.celery import app
from main.models import Page


@app.task(time_limit=10)
def update_counter(page_id):
    try:
        page = Page.objects.get(id=page_id)
        page.increment_counter()
    except SoftTimeLimitExceeded:
        logging.warning(f"TimeOut for Page {page_id} ")
    except Page.DoesNotExist:
        logging.warning(f"Not exists Page {page_id} ")

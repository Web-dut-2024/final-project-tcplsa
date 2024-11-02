from django.apps import AppConfig
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import main

class HeadlinesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "headlines"
    def ready(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(main, 'cron', hour=0, minute=12)  # 每天零点运行
        scheduler.start()

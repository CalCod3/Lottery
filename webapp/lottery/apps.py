from django.apps import AppConfig


class LotteryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lottery'
    
    def ready(self):
        from .helpers import start
        start()

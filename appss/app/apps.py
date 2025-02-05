from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appss.app'

    # import Book from models.lol.py
    def ready(self):
        from appss.app.models.lol import Book  # noqa

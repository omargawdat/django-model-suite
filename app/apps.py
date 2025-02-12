from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    # def ready(self):
    #     from app.admin.testmodelrelated import admin  # noqa

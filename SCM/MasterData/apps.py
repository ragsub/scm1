from django.apps import AppConfig


class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SCM.MasterData'

    def ready(self):
        import SCM.MasterData.signals
from django.apps import AppConfig

class SeimliteappConfig(AppConfig):
    name = 'seimLiteApp'

    def ready(self):
        import seimLiteApp.signals

from django.apps import AppConfig



class SiteSecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_sec'


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_sec'

    def ready(self):
        import site_sec.signals
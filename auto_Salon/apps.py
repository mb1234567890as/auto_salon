from django.apps import AppConfig


class AutoSalonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto_Salon'
    verbose_name = 'Авто салон'
    verbose_name_plural = 'Авто салоны'

    # def ready(self):
    #     print('dbins app ready')
    #     import auto_salon.signals

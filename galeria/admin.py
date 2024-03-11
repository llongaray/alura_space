from django.contrib import admin
from galeria.models import Fotografia
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.apps import apps

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "foto", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

class MeuAdminSite(AdminSite):
    site_title = 'Alura Space - Admin'
    site_header = 'Alura Space - Admin'
    index_title = 'Alura Space - Admin'

    def has_model_perm(self, user, model):
        return user.has_perm('%s.view_%s' % (model._meta.app_label, model._meta.model_name))

    def register_all_models(self, user):
        for app_config in apps.get_app_configs():
            for model in app_config.get_models():
                if self.has_model_perm(user, model):
                    self.register(model)

meu_admin_site = MeuAdminSite(name='meuadmin')
# Registre os modelos do Django no seu admin personalizado
meu_admin_site.register_all_models(User.objects.get(username='Admin'))

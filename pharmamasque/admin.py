from django.contrib import admin
from pharmamasque.models import Client


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client,ClientAdmin)
# Register your models here.

from django.contrib import admin

from .models import Client, ClientData

admin.site.register(Client)
admin.site.register(ClientData)

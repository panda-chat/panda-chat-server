from django.contrib import admin

from .models import Client, Message


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created")


admin.site.register(Client, BaseAdmin)
admin.site.register(Message, BaseAdmin)

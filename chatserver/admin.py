from django.contrib import admin

from .models import Client, Message


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Client)
admin.site.register(Message, MessageAdmin)

from django.contrib import admin
from django.utils.html import mark_safe

from .models import Client, Message


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created")


class MessageAdmin(BaseAdmin):
    readonly_fields = BaseAdmin.readonly_fields + ("img",)

    def img(self, obj):
        """This function allows images to be viewed directly in the admin site."""
        return mark_safe(
            f"<img src='/{obj.image.url}' width='{obj.image.width}' height='{obj.image.height}' />"
        )


admin.site.register(Client, BaseAdmin)
admin.site.register(Message, MessageAdmin)

# Replaces the `sender_name` string field with `sender` foreign key.
#
# This is done by creating an "NONE" user, and assigning that user as the sender for all existing messages.
#
# Also, all existing message contents have their `sender_name` string prepended to the message so that information isn't lost.

from django.db import migrations, models
from django.db.models import F, Value
from django.db.models.functions import Concat
import django.db.models.deletion


def create_and_set_default_user(apps, schema_editor):
    User = apps.get_model("chatserver", "User")
    Message = apps.get_model("chatserver", "Message")

    # mangled password hash so no one can sign in as this user
    default_user = User(
        username="NONE",
        password_hash="100000$P0yGGGGBFqrSrBBBBgOBUiSMASs=$T0qY4LN59E/z90llllPPSnosIflfpSBhJ0LLLLRSNcc=",
    )
    default_user.save()

    Message.objects.all().update(sender=default_user)


def add_sender_name_to_content(apps, schema_editor):
    Message = apps.get_model("chatserver", "Message")
    Message.objects.all().update(
        content=Concat(F("sender_name"), Value(": "), F("content"))
    )


def reverse_func(apps, schema_editor):
    pass  # not worried about reverting


class Migration(migrations.Migration):

    dependencies = [("chatserver", "0006_auto_20190301_1624")]

    operations = [
        # Make temporarily-nullable sender field.
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="chatserver.User",
            ),
        ),
        migrations.RunPython(create_and_set_default_user, reverse_func),
        # Make the sender field non-nullable now that they're all set.
        migrations.AlterField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="chatserver.User"
            ),
        ),
        migrations.RunPython(add_sender_name_to_content, reverse_func),
        # Remove the sender_name field now that we've preserved it.
        migrations.RemoveField(model_name="message", name="sender_name"),
    ]

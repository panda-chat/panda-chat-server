# Generated by Django 2.1.4 on 2019-01-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("chatserver", "0003_auto_20190104_1310")]

    operations = [
        migrations.RemoveField(model_name="message", name="sender"),
        migrations.AddField(
            model_name="message",
            name="sender_name",
            field=models.CharField(default="Unknown", max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(name="Client"),
    ]

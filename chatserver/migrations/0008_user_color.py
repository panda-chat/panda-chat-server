# Generated by Django 2.1.4 on 2019-03-05 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("chatserver", "0007_replace_sender_name_with_sender")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="color",
            field=models.CharField(default="#000000", max_length=7),
        )
    ]
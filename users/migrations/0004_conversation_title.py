# Generated by Django 5.0.1 on 2024-02-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_conversation_message_delete_newchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

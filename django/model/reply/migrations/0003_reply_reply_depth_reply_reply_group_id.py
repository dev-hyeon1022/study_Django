# Generated by Django 4.2.3 on 2023-08-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0002_reply_reply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_depth',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_group_id',
            field=models.IntegerField(null=True),
        ),
    ]

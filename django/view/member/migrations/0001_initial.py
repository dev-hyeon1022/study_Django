# Generated by Django 4.2.4 on 2023-08-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('member_email', models.CharField(max_length=200, unique=True)),
                ('member_password', models.CharField(max_length=200)),
                ('member_name', models.CharField(max_length=200)),
                ('member_age', models.PositiveSmallIntegerField(default=0)),
                ('member_birth', models.DateField()),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
    ]
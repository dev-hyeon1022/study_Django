# Generated by Django 4.2.3 on 2023-08-04 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_pay_product_count_pay_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pay',
            old_name='product_price',
            new_name='product_total_price',
        ),
    ]
# Generated by Django 4.2.4 on 2023-11-24 05:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0012_remove_borrow_fine_alter_borrow_borrow_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='remaining_day',
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

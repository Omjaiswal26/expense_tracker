# Generated by Django 4.1 on 2024-05-09 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0002_alter_tracker_expense_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='expense_name',
            new_name='expense_type',
        ),
    ]

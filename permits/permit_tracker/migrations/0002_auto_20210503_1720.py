# Generated by Django 3.2 on 2021-05-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permit',
            old_name='type',
            new_name='permit_type',
        ),
        migrations.AddField(
            model_name='permit',
            name='name',
            field=models.CharField(default='A10', max_length=50),
        ),
    ]
# Generated by Django 3.0.14 on 2023-04-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_auto_20230403_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]

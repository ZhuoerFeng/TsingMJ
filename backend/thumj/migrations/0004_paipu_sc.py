# Generated by Django 3.2 on 2023-10-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumj', '0003_remove_paipu_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='paipu',
            name='sc',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]

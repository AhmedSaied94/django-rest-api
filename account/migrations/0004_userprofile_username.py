# Generated by Django 3.2.9 on 2021-11-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211114_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='AhmedSaied94', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]

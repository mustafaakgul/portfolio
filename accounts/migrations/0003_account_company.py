# Generated by Django 3.2.3 on 2021-05-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
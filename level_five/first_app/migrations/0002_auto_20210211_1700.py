# Generated by Django 3.1.6 on 2021-02-11 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfolio_site',
            new_name='portfolio_site',
        ),
    ]

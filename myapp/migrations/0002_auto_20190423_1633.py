# Generated by Django 2.1.4 on 2019-04-23 10:33

import ckeditor.fields
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uconfig',
            field=jsonfield.fields.JSONField(blank=True, default={'delay': 'example.com', 'emaill': 'Email Is Empty!', 'host_con': 'not ok', 'imap': 'IMAP Is Empty!', 'name': 'Name Is Empty!', 'nrdelay': 'example.com', 'pass': 'Password Is Empty!', 'port': 'Port Is Empty!', 'smtp': 'SMTP Is Empty!'}),
        ),
        migrations.AlterField(
            model_name='temps',
            name='delay',
            field=models.IntegerField(default=456),
        ),
        migrations.AlterField(
            model_name='temps',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, default='Email Template- Is Blank!'),
        ),
    ]

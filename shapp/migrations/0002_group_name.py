# Generated by Django 4.2.7 on 2023-12-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='how', help_text='Имя группы', max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.2.1 on 2025-07-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('free', '자유'), ('diary', '일기'), ('activity', '활동')], default='free', max_length=20),
        ),
    ]

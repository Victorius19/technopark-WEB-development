# Generated by Django 3.2.8 on 2021-12-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_answers_count_question_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-10 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='catalog.book'),
        ),
    ]

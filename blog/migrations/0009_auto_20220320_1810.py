# Generated by Django 2.2.26 on 2022-03-20 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220307_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pdated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新日時'),
        ),
    ]

# Generated by Django 5.2 on 2025-04-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0003_recipie_recepie_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipie',
            name='recepie_view_count',
            field=models.IntegerField(default=1),
        ),
    ]

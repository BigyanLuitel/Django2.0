# Generated by Django 5.2 on 2025-04-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0002_recipie_user_alter_recipie_recepie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='recepie_view_count',
            field=models.IntegerField(default=0),
        ),
    ]

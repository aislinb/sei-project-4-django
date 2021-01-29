# Generated by Django 3.1.5 on 2021-01-29 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='crops.crop'),
        ),
    ]
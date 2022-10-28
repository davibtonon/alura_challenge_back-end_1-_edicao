# Generated by Django 4.0.3 on 2022-10-28 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos_api', '0003_video_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='videos_api.categoria'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-18 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201118_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resumes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='user.resume'),
            preserve_default=False,
        ),
    ]

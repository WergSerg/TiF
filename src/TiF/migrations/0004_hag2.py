# Generated by Django 3.2.9 on 2021-11-25 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiF', '0002_auto_20211122_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hag2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name2', models.CharField(max_length=100)),
                ('qweqw', models.CharField(max_length=100)),
                ('text2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='te', to='TiF.text')),
            ],
        ),
    ]

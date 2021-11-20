# Generated by Django 3.2.9 on 2021-11-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorys', to='TiF.category')),
            ],
        ),
        migrations.CreateModel(
            name='Mpaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=300)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('timeOfCreate', models.DateTimeField(auto_now_add=True)),
                ('timeOfUpadate', models.DateTimeField(auto_now_add=True)),
                ('mpaa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mpaa', to='TiF.mpaa')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('ban', models.BooleanField()),
                ('can_post_texts', models.BooleanField()),
                ('publicName', models.CharField(max_length=128)),
                ('contact', models.CharField(max_length=256, null=True)),
                ('about', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextDep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_deps', to='TiF.foundation')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_deps', to='TiF.text')),
            ],
        ),
        migrations.AddField(
            model_name='text',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='TiF.user'),
        ),
        migrations.AddField(
            model_name='text',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='TiF.choice'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(max_length=1000)),
                ('timeOfCreate', models.DateTimeField(auto_now_add=True)),
                ('timeOfUpadate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mess', to='TiF.user')),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TiF.user')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagname', to='TiF.text')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='TiF.user')),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='TiF.text')),
            ],
        ),
    ]

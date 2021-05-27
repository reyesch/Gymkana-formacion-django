# Generated by Django 2.2 on 2021-05-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
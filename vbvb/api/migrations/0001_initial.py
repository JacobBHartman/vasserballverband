# Generated by Django 2.1.4 on 2018-12-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=40)),
                ('place', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
        ),
    ]

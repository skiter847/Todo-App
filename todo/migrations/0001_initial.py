# Generated by Django 3.1.2 on 2020-10-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=20)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]

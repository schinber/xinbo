# Generated by Django 2.2.5 on 2019-09-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(default='ls', max_length=100)),
                ('password', models.CharField(default='toor', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]

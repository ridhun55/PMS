# Generated by Django 3.0.2 on 2020-02-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.15 on 2022-12-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('penulis', models.CharField(max_length=40)),
                ('penerbit', models.CharField(max_length=40)),
                ('jumlah', models.IntegerField(null=True)),
            ],
        ),
    ]

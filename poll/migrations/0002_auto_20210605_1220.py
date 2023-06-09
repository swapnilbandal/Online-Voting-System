# Generated by Django 3.1.7 on 2021-06-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('desc', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Symbol'),
        ),
    ]

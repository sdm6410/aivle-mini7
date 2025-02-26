# Generated by Django 3.2 on 2022-11-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AImodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ai_file', models.FileField(blank=True, upload_to='model/')),
                ('ai_version', models.CharField(default=1.0, max_length=50)),
                ('is_selected', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('answer', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

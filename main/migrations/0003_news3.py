# Generated by Django 5.0.6 on 2024-07-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news2'),
    ]

    operations = [
        migrations.CreateModel(
            name='News3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='new3_images/')),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]
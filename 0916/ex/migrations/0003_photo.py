# Generated by Django 3.1 on 2020-09-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='제목')),
                ('photo', models.ImageField(upload_to='%d')),
            ],
        ),
    ]

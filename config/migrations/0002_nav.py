# Generated by Django 4.2.2 on 2023-07-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('link', models.URLField(verbose_name='链接')),
                ('status', models.IntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1)),
            ],
            options={
                'verbose_name': '导航',
                'verbose_name_plural': '导航',
            },
        ),
    ]

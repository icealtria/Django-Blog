# Generated by Django 4.2.2 on 2023-06-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_desc_alter_post_body_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(0, 'Draft'), (1, 'Published')], max_length=10),
        ),
    ]

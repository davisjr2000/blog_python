# Generated by Django 2.0.3 on 2018-12-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post Title', max_length=100),
            preserve_default=False,
        ),
    ]

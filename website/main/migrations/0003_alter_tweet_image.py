# Generated by Django 4.2.3 on 2023-07-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_tweet_images_path_tweet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.FileField(upload_to='users/<django.db.models.fields.related.ForeignKey>/img'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_vues_tweet_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(default='178348.jpg', upload_to='users/<django.db.models.fields.related.ForeignKey>/img/'),
        ),
    ]
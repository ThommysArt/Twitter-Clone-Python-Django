# Generated by Django 4.2.3 on 2023-07-23 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_tweet_comments_alter_tweet_likes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='vues',
            new_name='views',
        ),
    ]
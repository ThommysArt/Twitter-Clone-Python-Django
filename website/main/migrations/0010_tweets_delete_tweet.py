# Generated by Django 4.2.3 on 2023-07-24 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_tweet_delete_tweets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('image', models.ImageField(default='', upload_to='media/')),
                ('likes', models.JSONField(default=None)),
                ('retweets', models.JSONField(default=None)),
                ('comments', models.JSONField(default=None)),
                ('views', models.JSONField(default=None)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]

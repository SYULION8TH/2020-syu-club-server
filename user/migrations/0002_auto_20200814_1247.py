# Generated by Django 3.1 on 2020-08-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsLike',
            fields=[
                ('posts_like_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='usersadditionalinfo',
            name='profile',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]

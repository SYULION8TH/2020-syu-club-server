# Generated by Django 3.1 on 2020-09-09 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubsmember',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='clubs',
            name='club_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.clubtypes'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clubsqna',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.clubs'),
        ),
        migrations.AlterField(
            model_name='clubsqna',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_posts', to='user.clubs'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postsreplies',
            name='parent_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reply', to='user.postsreplies'),
        ),
        migrations.AlterField(
            model_name='postsreplies',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.posts'),
        ),
        migrations.AlterField(
            model_name='postsreplies',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postsviews',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='view', to='user.posts'),
        ),
        migrations.AlterField(
            model_name='postsviews',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qnareplies',
            name='parent_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='user.qnareplies'),
        ),
        migrations.AlterField(
            model_name='qnareplies',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.clubsqna'),
        ),
        migrations.AlterField(
            model_name='usersadditionalinfo',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='add_info', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

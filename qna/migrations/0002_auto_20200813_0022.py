# Generated by Django 3.1 on 2020-08-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna_comment',
            name='qna',
        ),
        migrations.DeleteModel(
            name='Qna',
        ),
        migrations.DeleteModel(
            name='Qna_Comment',
        ),
    ]

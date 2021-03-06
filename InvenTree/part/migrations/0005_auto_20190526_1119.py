# Generated by Django 2.2 on 2019-05-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0004_auto_20190525_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='revision',
            field=models.CharField(blank=True, help_text='Part rerevision code', max_length=32),
        ),
        migrations.AlterUniqueTogether(
            name='part',
            unique_together={('name', 'revision')},
        ),
        migrations.RemoveField(
            model_name='part',
            name='variant',
        ),
    ]

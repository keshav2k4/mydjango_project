# Generated by Django 5.2 on 2025-04-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_teacher_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='Name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='Tsubject',
            field=models.CharField(default='Physics', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Tname',
            field=models.CharField(max_length=30),
        ),
    ]

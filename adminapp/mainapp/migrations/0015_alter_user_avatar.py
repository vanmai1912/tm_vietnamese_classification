# Generated by Django 4.1.5 on 2023-01-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_survey_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m'),
        ),
    ]
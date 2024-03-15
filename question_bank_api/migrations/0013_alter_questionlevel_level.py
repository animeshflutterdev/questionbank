# Generated by Django 4.1.12 on 2024-03-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank_api", "0012_alter_questionlevel_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionlevel",
            name="level",
            field=models.CharField(
                choices=[("1", "Easy"), ("2", "Medium"), ("3", "Hard")], max_length=1
            ),
        ),
    ]
# Generated by Django 4.1.12 on 2024-03-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank_api", "0013_alter_questionlevel_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionbank",
            name="image",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

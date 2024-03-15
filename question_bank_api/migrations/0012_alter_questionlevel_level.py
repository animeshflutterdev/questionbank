# Generated by Django 4.1.12 on 2024-03-13 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank_api", "0011_alter_questionlevel_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionlevel",
            name="level",
            field=models.ForeignKey(
                choices=[
                    ("1", "Level Easy"),
                    ("2", "Level Medium"),
                    ("3", "Level Hard"),
                ],
                on_delete=django.db.models.deletion.CASCADE,
                to="question_bank_api.questionlevel",
            ),
        ),
    ]
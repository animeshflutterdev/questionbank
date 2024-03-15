# Generated by Django 4.1.12 on 2024-03-13 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank_api", "0009_remove_questionbank_point_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionlevel",
            name="level",
            field=models.ForeignKey(
                choices=[("1", "Easy"), ("2", "Medium"), ("3", "Hard")],
                max_length=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="question_bank_api.questionlevel",
            ),
        ),
    ]

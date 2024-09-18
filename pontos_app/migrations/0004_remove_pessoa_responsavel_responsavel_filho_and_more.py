# Generated by Django 4.2.11 on 2024-09-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pontos_app", "0003_rename_filho_pontos_responsavel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pessoa",
            name="responsavel",
        ),
        migrations.CreateModel(
            name="Responsavel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pessoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pontos_app.pessoa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Filho",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "filho",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pontos_app.pessoa",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pontos",
            name="filho",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="pontos_app.filho",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pontos",
            name="responsavel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pontos_app.responsavel"
            ),
        ),
    ]

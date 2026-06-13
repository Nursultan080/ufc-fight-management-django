from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=140, verbose_name="Название турнира")),
                ("event_date", models.DateField(verbose_name="Дата")),
                ("city", models.CharField(max_length=80, verbose_name="Город")),
                ("country", models.CharField(max_length=80, verbose_name="Страна")),
            ],
            options={
                "verbose_name": "Турнир",
                "verbose_name_plural": "Турниры",
                "db_table": "events",
                "ordering": ["-event_date"],
            },
        ),
        migrations.CreateModel(
            name="WeightClass",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("max_weight_lb", models.PositiveIntegerField(verbose_name="Лимит веса, lb")),
            ],
            options={
                "verbose_name": "Весовая категория",
                "verbose_name_plural": "Весовые категории",
                "db_table": "weight_classes",
                "ordering": ["max_weight_lb"],
            },
        ),
        migrations.CreateModel(
            name="Fighter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120, verbose_name="Имя бойца")),
                ("nickname", models.CharField(blank=True, max_length=80, verbose_name="Прозвище")),
                ("country", models.CharField(max_length=80, verbose_name="Страна")),
                ("wins", models.PositiveIntegerField(default=0, verbose_name="Победы")),
                ("losses", models.PositiveIntegerField(default=0, verbose_name="Поражения")),
                (
                    "weight_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="fighters",
                        to="ufc_app.weightclass",
                        verbose_name="Весовая категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Боец",
                "verbose_name_plural": "Бойцы",
                "db_table": "fighters",
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="Fight",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rounds_scheduled", models.PositiveSmallIntegerField(default=3, verbose_name="Раундов запланировано")),
                (
                    "event",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="fights", to="ufc_app.event", verbose_name="Турнир"),
                ),
                (
                    "fighter_blue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="blue_corner_fights",
                        to="ufc_app.fighter",
                        verbose_name="Синий угол",
                    ),
                ),
                (
                    "fighter_red",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="red_corner_fights",
                        to="ufc_app.fighter",
                        verbose_name="Красный угол",
                    ),
                ),
                (
                    "weight_class",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="ufc_app.weightclass", verbose_name="Весовая категория"),
                ),
            ],
            options={
                "verbose_name": "Бой",
                "verbose_name_plural": "Бои",
                "db_table": "fights",
                "ordering": ["event", "id"],
            },
        ),
        migrations.CreateModel(
            name="FightResult",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("KO/TKO", "KO/TKO"),
                            ("Submission", "Submission"),
                            ("Decision", "Decision"),
                            ("Draw", "Draw"),
                            ("No Contest", "No Contest"),
                        ],
                        max_length=30,
                        verbose_name="Метод",
                    ),
                ),
                ("round_finished", models.PositiveSmallIntegerField(default=1, verbose_name="Раунд")),
                ("time_finished", models.CharField(default="5:00", max_length=5, verbose_name="Время")),
                (
                    "fight",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="result", to="ufc_app.fight", verbose_name="Бой"),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="wins_results",
                        to="ufc_app.fighter",
                        verbose_name="Победитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат боя",
                "verbose_name_plural": "Результаты боёв",
                "db_table": "fight_results",
                "ordering": ["fight"],
            },
        ),
    ]

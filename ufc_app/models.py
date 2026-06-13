from django.db import models


class WeightClass(models.Model):
    name = models.CharField("Название", max_length=100)
    max_weight_lb = models.PositiveIntegerField("Лимит веса, lb")

    class Meta:
        db_table = "weight_classes"
        ordering = ["max_weight_lb"]
        verbose_name = "Весовая категория"
        verbose_name_plural = "Весовые категории"

    def __str__(self):
        return f"{self.name} ({self.max_weight_lb} lb)"


class Fighter(models.Model):
    full_name = models.CharField("Имя бойца", max_length=120)
    nickname = models.CharField("Прозвище", max_length=80, blank=True)
    country = models.CharField("Страна", max_length=80)
    weight_class = models.ForeignKey(
        WeightClass,
        on_delete=models.PROTECT,
        related_name="fighters",
        verbose_name="Весовая категория",
    )
    wins = models.PositiveIntegerField("Победы", default=0)
    losses = models.PositiveIntegerField("Поражения", default=0)

    class Meta:
        db_table = "fighters"
        ordering = ["full_name"]
        verbose_name = "Боец"
        verbose_name_plural = "Бойцы"

    def __str__(self):
        return self.full_name


class Event(models.Model):
    title = models.CharField("Название турнира", max_length=140)
    event_date = models.DateField("Дата")
    city = models.CharField("Город", max_length=80)
    country = models.CharField("Страна", max_length=80)

    class Meta:
        db_table = "events"
        ordering = ["-event_date"]
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"

    def __str__(self):
        return self.title


class Fight(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="fights", verbose_name="Турнир")
    fighter_red = models.ForeignKey(
        Fighter,
        on_delete=models.PROTECT,
        related_name="red_corner_fights",
        verbose_name="Красный угол",
    )
    fighter_blue = models.ForeignKey(
        Fighter,
        on_delete=models.PROTECT,
        related_name="blue_corner_fights",
        verbose_name="Синий угол",
    )
    weight_class = models.ForeignKey(WeightClass, on_delete=models.PROTECT, verbose_name="Весовая категория")
    rounds_scheduled = models.PositiveSmallIntegerField("Раундов запланировано", default=3)

    class Meta:
        db_table = "fights"
        ordering = ["event", "id"]
        verbose_name = "Бой"
        verbose_name_plural = "Бои"

    def __str__(self):
        return f"{self.fighter_red} vs {self.fighter_blue}"


class FightResult(models.Model):
    METHOD_CHOICES = [
        ("KO/TKO", "KO/TKO"),
        ("Submission", "Submission"),
        ("Decision", "Decision"),
        ("Draw", "Draw"),
        ("No Contest", "No Contest"),
    ]

    fight = models.OneToOneField(Fight, on_delete=models.CASCADE, related_name="result", verbose_name="Бой")
    winner = models.ForeignKey(
        Fighter,
        on_delete=models.PROTECT,
        related_name="wins_results",
        verbose_name="Победитель",
        blank=True,
        null=True,
    )
    method = models.CharField("Метод", max_length=30, choices=METHOD_CHOICES)
    round_finished = models.PositiveSmallIntegerField("Раунд", default=1)
    time_finished = models.CharField("Время", max_length=5, default="5:00")

    class Meta:
        db_table = "fight_results"
        ordering = ["fight"]
        verbose_name = "Результат боя"
        verbose_name_plural = "Результаты боёв"

    def __str__(self):
        return f"{self.fight}: {self.method}"

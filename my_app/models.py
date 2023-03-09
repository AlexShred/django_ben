from django.db import models


class TestModel(models.Model):
    string = models.CharField(max_length=20, verbose_name="Нвзвание поля 1")
    date = models.DateField(verbose_name="DAte 1")
    datetime = models.DateTimeField(verbose_name="ДАта и время")
    checkbox = models.BooleanField(verbose_name="Чек бокс")
    integer = models.IntegerField(verbose_name="ЧИсло")
    choices = models.IntegerField(verbose_name="ВЫборка", choices=(
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
    ))
    nullable = models.TextField(verbose_name="Какойто текст", blank=True, null=True)
    # nullable = models.TextField(verbose_name="Какойто текст", default="dsad")

    def __str__(self):
        return f"Тестовая модель номер {self.id}"


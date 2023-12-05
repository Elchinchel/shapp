from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255, help_text='Имя группы')

    def __str__(self) -> str:
        return f'Группа {self.name}'

    @property
    def students(self):
        return Student.objects.filter(group__name=self.name)

    @property
    def subjects(self):
        return Subject.objects.filter(group__name=self.name)


class Student(models.Model):
    name = models.CharField(max_length=255, help_text='ФИО')
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    bdate = models.DateField(help_text='Дата рождения')

    def __str__(self) -> str:
        return f'{self.name}'


class Subject(models.Model):
    name = models.CharField(max_length=255, help_text='Наименование дисциплины')
    group = models.ManyToManyField(Group)

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def groups(self):
        return self.group.all()

from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.position})"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='visits')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='visits')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField()
    visit_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Посещение {self.client} ({self.visit_type}) {self.visit_date}"

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'


class VisitService(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='visit_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='visit_services')

    def __str__(self):
        return f"{self.visit} - {self.service}"

    class Meta:
        verbose_name = 'Связь посещения и услуги'
        verbose_name_plural = 'Связи посещений и услуг'
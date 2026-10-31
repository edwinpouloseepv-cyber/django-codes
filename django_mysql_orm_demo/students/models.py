from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Task(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
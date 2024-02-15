from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 200, default="")
    description = models.TextField(default="")
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Example(models.Model):
    cont = models.CharField(max_length = 200)
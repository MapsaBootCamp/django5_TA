from django.db import models


# Create your models here.
class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    due_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=300)
    cat = models.ForeignKey(to='Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.cat.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

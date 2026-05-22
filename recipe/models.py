from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __iter__(self):
        return iter(self.recipe_set.all())